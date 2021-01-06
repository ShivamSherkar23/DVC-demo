import dvc.api

resource_url = dvc.api.get_url(
    'get-started/data.xml',
    repo='https://github.com/iterative/dataset-registry'
)
print("output from the get url method is ")
print(resource_url)
