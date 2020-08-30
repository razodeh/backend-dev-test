## Ingestion plan for a production-ready system

### Scalability

Scaling Ingestion to a production-grade system needs
a crucial key-points to tackle:

1. Containerization (Using Docker, or similar)
2. Containers Orchestration (Using K8s, or similar)
3. CI/CD pipeline
4. Ingested Data Store Multi-Leader Replication (since it is Write-Extensive).

### Testability

In order for Ingestion App to be a production-grade app,
we need to focus more on BDD use cases, to be more inclusive
of the use cases, and Including our testing framework tests, as a part of our
CI/CD pipeline.

Also having Unit tests that covers all parts of the
data pipeline processing logic, is highly needed since
we are dealing with an unstructured data, that needs to be
ingested and stored. 


### Security

Securing our ingestion pipeline, is a very important step
to prevent any unauthorized access to our pipeline,
through isolating it on its own virtual private cloud
infrastructure along with our existing data pipelines.


> I hope I covered most of the aspects, that is going
> to allow IngestionApp to be production-ready data
> ingestion pipeline.

#### Thanks