# Fertility-Prediction


## Overview

The **Fertility Prediction** project aims to predict whether the semen of a man is normal or otherwise. It utilizes a Flask web application and is deployed on AWS Elastic Beanstalk. The prediction model is built using machine learning techniques like catboost and xgboost.

## Repository Structure

- **.ebextensions**: Configuration files for AWS Elastic Beanstalk.
- **artifacts**: Artifacts generated during the deployment process.
- **catboost_info**: CatBoost model information.
- **data**: Dataset and related data files.
- **src**: Source code for the Flask app and machine learning model.
- **templates**: HTML templates for the Flask app.
- **LICENSE**: The project's license information.
- **application.py**: Main Flask application file.
- **requirements.txt**: List of Python dependencies.
- **setup.py**: Setup file for packaging and distribution.

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fertility-prediction.git
   ```

2. Install dependencies:

   ```bash
   cd fertility-prediction
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python application.py
   ```

   Visit `http://localhost:XXXX` in your web browser.

## Deployment on AWS Elastic Beanstalk

The project is designed to be deployed on AWS Elastic Beanstalk. Follow these general steps for deployment:

1. Set up an AWS Elastic Beanstalk environment.
2. Configure the necessary environment variables.
3. Deploy the application to Elastic Beanstalk.

link here: Akram-env.eba-u7sdapzq.us-east-2.elasticbeanstalk.com not active now .

## License

This project is licensed under the [LICENSE NAME](LICENSE) - see the [LICENSE](LICENSE) file for details.

