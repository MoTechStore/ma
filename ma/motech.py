def get_article_info(url):
  a = Article(url)
  try:
    a.download()
    a.parse()
    a.nlp()
    success, checked_kws = checkif_kw_exist(req_keywords, a.text.split())
    if success:
      return [url, a.publish_date, a.title, a.text]
    else: 
      return False
  except ArticleException as ae:
     print (ae)
     return False
  except Exception as e:
     print(e)
     return False
