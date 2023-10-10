run postgres docker: 	
docker run -d --name postgres -p 5433:5432 -v /tmp/database:/var/lib/postgresql/data -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password postgres

problemas:
- insercao de dados que ja existem, isso se trata?
- dados sem identificador unico, em que momento se adiciona um id unico a cada?