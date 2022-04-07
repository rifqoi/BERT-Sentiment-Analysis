import twint
config = twint.Config()
config.Search = "formula e anies jakarta"
config.Limit = 30000
config.Store_csv = True
config.Resume = '1475257348864155650'
config.Output = "peduli3.csv"
twint.run.Search(config)
