
#from haystack import indexes
#from models import Account
#import datetime


# class AccountIndex(indexes.SearchIndex, indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#    upld_date = indexes.DateTimeField(model_attr='upld_date')

#   content_auto = indexes.EdgeNgramField(model_attr='name')
#   content_auto = indexes.EdgeNgramField(model_attr='code')
#   content_auto = indexes.EdgeNgramField(model_attr='status')

#   def get_model(self):
#       return Account

#   def index_queryset(self, using=None):
#       return self.get_model().objects.all()
