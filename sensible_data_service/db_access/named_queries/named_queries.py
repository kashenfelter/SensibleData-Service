from db_access.named_queries import stops_named_queries, device_inventory_named_queries, \
	resampled_location_named_queries, facebook_named_queries, questionnaire_named_queries, funf_named_queries, data_quality_named_queries

NAMED_QUERIES = {}
NAMED_QUERIES.update(funf_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(questionnaire_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(facebook_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(stops_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(device_inventory_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(resampled_location_named_queries.NAMED_QUERIES)
NAMED_QUERIES.update(data_quality_named_queries.NAMED_QUERIES)
