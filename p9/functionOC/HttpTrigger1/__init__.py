import logging
import azure.functions as func
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO


def get_content_based_recommendation(user_id, clicks, embeddings, n_reco=5):
    '''Return 5 recommended articles ID to user'''

    # Get the list of articles viewed by the user
    var = clicks.loc[clicks.user_id == user_id]['article_id'].to_list()

    # Get the list of unique article_id in clicks
    list_article_id = sorted(list(clicks.article_id.unique()))

    # Retrieve the corresponding index of the articles viewed by user_id in var
    idx_var = []
    for i in range(0, len(var)):
        for idx, item in enumerate(list(list_article_id)):
            if item == var[i]:
                idx_var.append(idx)

    # Select the last element of the list
    value = idx_var[-1]
    # print(value)

    # Compute the cosine similarity
    emb = embeddings
    distances = cosine_similarity([emb[value]], emb)[0]

    # Save the result in Pandas DataFrame
    df_recommendation = pd.DataFrame(list(zip(list_article_id, distances)), columns=(["recommended_article_id", "similarity"]))
    
    # Sort the dataframe by similarity
    df_recommendation.sort_values(by='similarity', ascending=False, inplace=True)

    # Exclude already viewed articles
    top_recommendation = df_recommendation[~df_recommendation.recommended_article_id.isin(var)]

    # Give the list of recommended articles
    result = list(top_recommendation["recommended_article_id"].iloc[:(n_reco)].values)

    return result


def main(req: func.HttpRequest, clicksBlob: func.InputStream, embeddingsBlob: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Load the data from AzureBlobStorage
    clicks = pd.read_csv(BytesIO(clicksBlob.read()), index_col=None, header=0)
    print('click: ', clicks.shape)
    embeddings = pd.read_pickle(BytesIO(embeddingsBlob.read()))
    print('emb ', embeddings.shape)

    # Put the mobile app userId param in a variable
    user_id = req.params.get('userId')
    
    if not user_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user_id = req_body.get('userId')

    if user_id:
        # Get the 5 articles' recommendations
        user_id = int(user_id)
        recommendations = get_content_based_recommendation(user_id, clicks, embeddings, n_reco=5)

        # Convert the list in string
        str_result = ' '.join(str(elem) + "," for elem in recommendations)

        # Delete the last comma
        result = str_result.rstrip(str_result[-1])

        # Template example is to return a sentence with the user_id
        return func.HttpResponse(result)

    else:
        return func.HttpResponse("This HTTP triggered function executed successfully. Please enter a userID.", status_code=200)
