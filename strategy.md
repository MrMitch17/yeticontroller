# Strategy for Cyberdyne

## Summary
We are looking to migrate and deploy an internal application to a public cloud.  This application is owned by the Active Targeting team within Cyberdyne and is responsible for the target selection and firing solutions for the eastern seaboard defence system.  It has become too cumbersome for the team to maintain both server infrastructure and manage a reliable development release cycle.


## Scope of Project
- Migrate application to run on a lambda within AWS
- Design a development pipeline that will do the following
		- Run unit tests
		- Check Code Coverage
		- Deploy to Staging on new commits for testing
		- Deploy to Production on new Releases

## Considerations
Cyberdyne maintains FedRAMP Moderate compliance.  All services and deployments must maintain these compliance standards.  While Liatrio is not responsible for issuing compliance, we are responsible for meeting requirements as directed by the client and external auditors found in the compliance worksheet provided by the customer.


We have chosen server-less for its ease of deployment and management for the system for the demo. 

##  Main Phases of Engagement

### Information Gathering
The first phase is to understand what is currently the way the team works and deploys software.  The main focus is a complete understanding of the application by Liatro Engineers and Principals.

 - Kick off and Introductions
 - Understanding and demonstrations of current workflows
 - Gather pain points
 - Current tools and processes


### Design
In this phase we will collaborate with product owners and developers to design a system and process that works for the team. Every team works differently and we need to come-up with something they can take ownership in.  Best way to do that is by including key stakeholders in early phases of the design.  This way the sense of ownership is early on in the process.

- Tool Selection
- MVP goal Setting
- Chargers on "Best Practices"
- Diagramming of **Existing** Processes and workflows
- Diagramming of **Future** Processes and workflows
- Expected Project Timelines and Resources needed

### Implementation
This phase is the "hands-on" portion of the engagement.  We reference the documentation created in the design phase and start building the actual implementation.  There will be discrete goals and accomplishments along this process.

- Regular check-ins with engineers to ensure project is on track.
- Regular check-ins with project stakeholders to communicate progress.


### Acceptance Testing and Hand-off
In this final phase, we will validate and test all functions and look for user testing and that they can manage the infrastructure and deployments themselves.

- Demonstrations of KT
- Documents and Readme's Reviewed and Accepted
- SOWs Reviewed and Signed off on.
