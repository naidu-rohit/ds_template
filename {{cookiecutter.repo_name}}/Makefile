.PHONY: setup clean_data train
	
env:
	conda env create --file environment.yml


clean:
	rm -R data/processed/*
	rm -R data/interim/*


format:
	black .


test:
	pytest tests


update_env:
	conda env update --prefix ./env --file environment.yml  --prune


preprocess:
	dagster pipeline execute -f {{cookiecutter.package_name}}/pipelines.py -n preprocess_pipeline -p dev

features:
	dagster pipeline execute -f {{cookiecutter.package_name}}/pipelines.py -n feature_eng_pipeline -p dev

train:
	dagster pipeline execute -f {{cookiecutter.package_name}}/pipelines.py -n train_pipeline -p dev

predict:
	dagster pipeline execute -f {{cookiecutter.package_name}}/pipelines.py -n train_pipeline -p dev



# DAGSTER_HOME=.dagster