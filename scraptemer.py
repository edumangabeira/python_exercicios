import tweepy
import csv
# coloque aqui as suas credenciais do seu app twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

'''
Abre arquivo e adiciona os dados, se você quiser que essa planilha seja apagada e novos dados sejam escritos,
 basta trocar o argumento 'a'(de append - adicionar) para 'w'(write - (sob)escrever).
'''
csvFile = open('temer.csv', 'a')
csvWriter = csv.writer(csvFile, lineterminator='\n')
'''
lista_hashtags:
Para adicionar as hashtags, basta agrupa-las sequencialmente no argumento 'q', por isso criei uma lista
contendo as hashtags desejadas, basta alterar essa lista
'''
lista_hashtags = ["#ficatemer", "#foratemer"]
hashtags = ''
for tag, hashtag in enumerate(lista_hashtags):
    hashtags = hashtags + hashtag

'''
SINCE:
O argumento 'since' deve ser usado para marcar a data inicial de coleta dos tweets.
Também é possível adicionar o argumento 'until' para dizer a data limite.

No atributo 'itens()' você pode selecionar a quantidade de tweets que deseja reunir.
'''
for tweet in tweepy.Cursor(api.search, q=hashtags, lang="pt-br", since="2018-03-20").items(100):
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
