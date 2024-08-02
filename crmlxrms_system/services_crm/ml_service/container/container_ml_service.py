from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("ML CRM Microservice - Container Diagram", direction="TB"):
    with SystemBoundary("ML CRM Microservice"):
        # Command Handlers
        train_model_command = Container(
            "TrainModelCommandHandler",
            "Python",
            "Handles requests to train new ML models"
        )
        
        update_model_command = Container(
            "UpdateModelCommandHandler",
            "Python",..add()
            "Handles requests to update existing ML models"
        )
        
        delete_model_command = Container(
            "DeleteModelCommandHandler",
            "Python",
            "Handles requests to delete ML models"
        )
        
        predict_command = Container(
            "PredictCommandHandler",
            "Python",
            "Handles prediction requests using trained ML models"
        )
        
        evaluate_model_command = Container(
            "EvaluateModelCommandHandler",
            "Python",
            "Handles requests to evaluate the performance of ML models"
        )

        # Query Handlers
        get_model_query = Container(
            "GetModelQueryHandler",
            "Python",
            "Handles requests to retrieve ML model details"
        )
        
        list_models_query = Container(
            "ListModelsQueryHandler",
            "Python",
            "Handles requests to list all ML models"
        )
        
        get_prediction_query = Container(
            "GetPredictionQueryHandler",
            "Python",
            "Handles requests to retrieve prediction results"
        )
        
        get_model_performance_query = Container(
            "GetModelPerformanceQueryHandler",
            "Python",
            "Handles requests to retrieve ML model performance metrics"
        )
        
        get_training_data_query = Container(
            "GetTrainingDataQueryHandler",
            "Python",
            "Handles requests to retrieve training data details"
        )
        
        # Databases
        ml_db = Database(
            "ML Database",
            "MongoDB",
            "Stores ML models, predictions, and performance metrics"
        )

        # Relationships
        train_model_command >> Relationship("Stores trained models in") >> ml_db
        update_model_command >> Relationship("Updates models in") >> ml_db
        delete_model_command >> Relationship("Removes models from") >> ml_db
        predict_command >> Relationship("Stores predictions in") >> ml_db
        evaluate_model_command >> Relationship("Stores evaluation metrics in") >> ml_db
        
        get_model_query << Relationship("Fetches model details from") << ml_db
        list_models_query << Relationship("Fetches model list from") << ml_db
        get_prediction_query << Relationship("Fetches predictions from") << ml_db
        get_model_performance_query << Relationship("Fetches performance metrics from") << ml_db
        get_training_data_query << Relationship("Fetches training data from") << ml_db
