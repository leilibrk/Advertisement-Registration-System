# Advertisement Registration System (2023)

This repository presents the Advertisement Registration System developed as part of the "Cloud Computing" course in 2023. The project aims to provide hands-on experience with cloud service systems while building an advanced advertisement registration platform.

## Project Overview

- **Goal:** Gain familiarity with cloud service systems by implementing an advertisement registration platform.
- **Implementation:** The project is implemented using Django, MySQL, and various cloud service systems.
- **Course:** Cloud Computing
- **Grade:** 19.87/20
- **Professor:** Dr. Javadi Method

## Implemented Features

The project leverages a variety of cloud service systems to streamline the advertisement registration process:

- **AWS S3:** The system utilizes Amazon S3 to store uploaded ad images securely.
- **Aiven:** Aiven is employed to manage and handle database operations using MySQL.
- **RabbitMQ:** The platform utilizes RabbitMQ for effective message queuing between components.
- **Mailgun:** The system integrates with Mailgun to send emails to users regarding their advertisement registration status.
- **Imagga:** Imagga's image recognition services are utilized for tagging and analysis of ad images.

## Workflow

1. User uploads an ad image.
2. The image is sent to Imagga for tagging.
3. Based on tags, the system accepts or rejects the image.
4. Approved images are stored in AWS S3.
5. An email is sent to the user using Mailgun to inform them of the registration status.

## Usage

To explore this project:

1. Clone the repository: `git clone https://github.com/leilibrk/advertisement-registration-system.git`
2. Review the code and documentation in the relevant directories for each cloud service integration and feature.
3. Experiment with the platform's functionality to understand its interaction with various cloud services.

## Acknowledgments

We extend our gratitude to Dr. Javadi for guiding us through the Cloud Computing course and inspiring us to build a sophisticated Advertisement Registration System using cloud services.

## Contributing

Contributions to this repository are welcomed! If you have ideas to enhance the system, improve integrations, or add new features, feel free to fork the repository and submit pull requests.

