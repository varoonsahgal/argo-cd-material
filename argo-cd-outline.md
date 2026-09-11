Intermediate Argo CD Operations
A two-day, hands-on course for DevOps engineers
Course Summary
This course prepares DevOps engineers to operate Argo CD as a reliable internal deployment platform. It is designed around a production architecture in which Argo CD runs on dedicated Rancher-managed Kubernetes clusters and deploys to separately registered workload clusters.
The course focuses on the most important operational areas: understanding an Argo CD Application at its core, deploying Helm-based applications, working safely with ApplicationSets and App-of-Apps, and keeping the platform secure, observable, stable, and recoverable.
This is an Argo CD operations course-not an Argo Workflows course. Argo Workflows is addressed only briefly so participants understand where it fits in the wider Argo ecosystem.
Target Audience
DevOps, CI/CD, and platform engineers who will host and maintain Argo CD
Engineers responsible for onboarding repositories, clusters, and deployment patterns
Engineers who will troubleshoot application delivery across lower and higher environments
A small number of software engineers may attend if they need deeper knowledge of Argo CD applications, deployment behavior, or API-based integration. Developer-only onboarding is better handled as a shorter follow-on session.
Prerequisites
Participants should be comfortable with:
Kubernetes resources, namespaces, RBAC, and basic troubleshooting
Git repositories, branches, pull requests, and commit history
Helm charts and values files
Basic use of kubectl, helm, and Git
Learning Objectives
By the end of the course, participants will be able to:
Explain how Argo CD continuously reconciles Git state with live Kubernetes state
Describe the role of each major Argo CD component and identify where failures occur
Configure Argo CD for a dedicated management-cluster and remote-workload-cluster model
Build and troubleshoot Application, ApplicationSet, and App-of-Apps structures
Deploy Helm applications and safely manage environment-specific configuration
Apply synchronization, promotion, RBAC, and AppProject guardrails
Diagnose repository, rendering, synchronization, health, and cluster-connectivity failures
Plan for high availability, monitoring, scaling, backup, recovery, upgrades, and custom builds
Course Design Assumptions
Primary audience: DevOps and platform engineers
Platform: Rancher-managed Kubernetes/RKE2
Argo CD topology: dedicated management clusters with registered workload clusters
Primary packaging method: Helm
Secondary configuration method: Kustomize where currently used
Key deployment patterns: ApplicationSets and App-of-Apps
Delivery format: approximately 50% guided instruction and 50% hands-on work
Class size: up to 20 participants
Day 1 - Understand, Configure, and Deploy with Argo CD
Day 1 establishes the mental model participants need before they manage complex patterns. The labs build one working deployment from Git through Argo CD to a remote workload cluster.
Session
Duration
Focus
1. GitOps and the Argo CD topology
45 min
Platform purpose, boundaries, and deployment flow
2. Argo CD architecture and the Application model
60 min
Components, reconciliation, health, sync, and ownership
Lab 1. Follow an application through reconciliation
45 min
Trace Git, rendered manifests, live state, and status
3. Production-oriented configuration
60 min
Installation choices, declarative setup, repositories, and clusters
Lab 2. Configure the platform and register a target
60 min
Repository onboarding and workload-cluster registration
4. Helm deployments, synchronization, and promotion
60 min
Rendering, drift, sync controls, ordering, and environments
Lab 3. Deploy, introduce drift, and recover
60 min
Helm deployment and controlled recovery


1. GitOps and the Argo CD Topology
Git as the desired-state source and audit trail
Continuous reconciliation, drift detection, and declarative recovery
The division of responsibility between CI and Argo CD
Argo CD compared with Argo Workflows
A production topology with dedicated Argo CD management clusters and registered workload clusters
Platform-team responsibilities versus application-team responsibilities
A complete deployment flow: Git change -> render -> compare -> synchronize -> health assessment
Key outcome: Participants can explain what Argo CD owns, what it does not own, and where it fits in a delivery platform.
2. Argo CD Architecture and the Application Model
API server, application controller, repository server, ApplicationSet controller, Redis, and supporting components
Desired state, live state, target state, and rendered manifests
The difference between sync status and health status
The Application resource: source, revision, path or chart, destination, project, and sync policy
Repository credentials, cluster credentials, resource tracking, and ownership
Refresh, compare, reconcile, and synchronize operations
Common causes of OutOfSync, Unknown, Progressing, and Degraded states
Lab 1: Follow an Application Through Reconciliation
Inspect an Application manifest and identify every external dependency
Commit a small change and observe the reconciliation flow
Compare desired, rendered, and live resources
Use the UI, CLI, and Kubernetes resources to locate status and events
3. Production-Oriented Configuration
Multi-tenant versus core installation models and why multi-tenant Argo CD fits this use case
Standard versus high-availability installation choices
Helm-based installation and declarative management of Argo CD itself
Namespace, ingress, TLS, DNS, and initial access considerations
Declarative repository and cluster onboarding
Registering remote workload clusters with least-privilege credentials
Webhooks versus polling and their network implications
Rancher/RKE2 considerations and separation between management and workload clusters
Configuration that should be stored in Git versus injected securely
The instructor demonstrates installation and high-availability configuration. Participants use a pre-provisioned, resettable environment so the lab focuses on meaningful platform configuration instead of waiting for clusters and controllers to initialize.
Lab 2: Configure the Platform and Register a Target
Connect a prepared Git repository
Register a separate workload cluster
Verify repository and cluster connectivity
Create a basic AppProject and Application declaratively
Confirm that Argo CD can render and compare the target application
4. Helm Deployments, Synchronization, and Promotion
How Argo CD uses Helm to render manifests rather than manage a traditional Helm release lifecycle
Chart sources, pinned revisions, values files, parameters, and environment overrides
Repository-layout options for reusable Helm deployments
Where Kustomize can complement Helm without creating unclear ownership
Manual versus automated synchronization
Pruning, self-healing, retries, timeouts, and safe sync options
Sync phases, waves, hooks, and resource ordering
Promotion through Git across development and higher environments
Roll-forward, rollback, and recovery tradeoffs
Guardrails against accidental pruning, cross-environment deployment, and mutable revisions
Lab 3: Deploy, Introduce Drift, and Recover
Deploy a Helm-based application to the registered workload cluster
Apply an environment-specific values file
Introduce live drift and observe Argo CD's response
Configure safe automated synchronization and self-healing
Introduce a rendering or ordering failure and recover through Git
Day 1 Outcome
Participants finish Day 1 with a working Git-to-Argo-CD-to-workload-cluster deployment and a repeatable method for locating failures along that path.
Day 2 - Scale the Pattern and Operate It Reliably
Day 2 applies the Day 1 model to more complex production patterns. The labs emphasize blast-radius control, troubleshooting, and production operations.
Session
Duration
Focus
5. ApplicationSets and App-of-Apps
60 min
Pattern mechanics, selection, ownership, and risk
Lab 4. Build and troubleshoot the patterns
75 min
Multi-environment generation and parent-child diagnosis
6. Security, multi-tenancy, and governance
45 min
AppProjects, SSO/RBAC, credentials, and policy boundaries
Lab 5. Enforce platform guardrails
45 min
Restrict sources, destinations, actions, and deletion behavior
7. Reliability, troubleshooting, and lifecycle operations
75 min
HA, scale, observability, incidents, upgrades, and recovery
Capstone. Restore an Argo CD deployment platform
90 min
Diagnose and recover a multi-layer failure scenario


5. ApplicationSets and App-of-Apps
ApplicationSets
How an ApplicationSet generates and owns Applications
List, cluster, Git, matrix, and merge generators
Go templating and failing safely on missing values
Multi-cluster and multi-environment targeting
Controlling whether generated Applications may be created, updated, or deleted
Reducing the blast radius of generator and template changes
Previewing generated output before rollout
Version-dependent features, such as progressive synchronization, and when not to depend on them
App-of-Apps
Root and child Applications and how ownership flows between them
Repository organization, naming, and responsibility boundaries
Resource ordering, pruning, cascading deletion, and circular dependency risks
Why multiple roots become difficult to reason about
Tracing failures from a root Application to the affected repository and child resource
Choosing the Right Pattern
Need
Prefer
Generate similar Applications from cluster or Git data
ApplicationSet
Bootstrap a known hierarchy of platform components
App-of-Apps
Manage many clusters or environments without duplication
ApplicationSet
Preserve a deliberate parent-child bootstrap structure
App-of-Apps
Combine both patterns
Only with explicit ownership and deletion boundaries


Lab 4: Build and Troubleshoot the Patterns
Generate Helm Applications for multiple target environments
Use labels and cluster data to control placement
Apply a protection policy that limits unintended Application deletion
Inspect a root and child Application hierarchy
Introduce a template or child-application error and trace it to the owning layer
Compare the operational impact of implementing the same scenario with each pattern
6. Security, Multi-Tenancy, and Governance
AppProjects as boundaries for source repositories, destinations, namespaces, and resource kinds
The difference between Argo CD RBAC and Kubernetes RBAC
SSO concepts, group-to-role mapping, and removal of routine administrator access
Least-privilege repository and workload-cluster credentials
Separation of duties between platform engineers and application teams
Managing secrets without committing plaintext values to Git
API accounts and tokens for approved automation
Auditability, deployment windows, and controls for higher environments
Security implications of allowing teams to create Applications or ApplicationSets
Lab 5: Enforce Platform Guardrails
Create a restricted AppProject
Permit an approved source, namespace, and workload cluster
Block an unauthorized destination and cluster-scoped resource
Compare an Argo CD authorization failure with a Kubernetes authorization failure
Protect generated Applications from unintended deletion
7. Reliability, Troubleshooting, and Lifecycle Operations
A Repeatable Troubleshooting Method
Validate the Git source and revision.
Validate repository access and manifest rendering.
Compare rendered state with live cluster state.
Inspect synchronization results, hooks, events, and Kubernetes health.
Inspect the responsible Argo CD component and its metrics.
Correct the declarative source and verify reconciliation.
Stability, Observability, and Scale
High-availability architecture and component failure behavior
Application-controller load, cluster sharding, and reconciliation queues
Repository-server memory, disk, concurrency, timeouts, and monorepo pressure
Webhook and reconciliation behavior
Prometheus metrics, dashboards, alerts, events, and notifications
Custom health checks, diff customizations, and reconcile optimizations
Avoiding ignore rules that conceal meaningful drift
Capacity factors: applications, resources, clusters, repositories, repository size, and change rate
Backup, Recovery, Upgrades, and Custom Builds
Argo CD's Kubernetes resources as persistent configuration and Redis as a disposable cache
Declarative configuration plus argocd admin export and import
Recovery when the Argo CD management cluster is lost
Upgrade planning, release notes, compatibility testing, and rollback criteria
Matching Argo CD and Kubernetes/RKE2 versions
Operational implications of an internal fork: upstream tracking, CVE response, image build and provenance, regression testing, release cadence, and minimizing divergence
Capstone: Restore an Argo CD Deployment Platform
Participants receive an environment containing several connected failures, such as:
A broken Helm values reference or rendering error
An ApplicationSet change with an unexpectedly large blast radius
A root or child Application ownership problem
An AppProject or Kubernetes RBAC denial
A disconnected workload cluster
A degraded workload combined with noisy or misleading drift
An Argo CD component under resource pressure
Participants must:
Identify the failure layer without making uncontrolled changes.
Use Argo CD and Kubernetes evidence to determine root cause.
Repair the desired state or platform configuration.
Verify reconciliation, synchronization, and application health.
Explain the guardrail or monitoring change that would prevent recurrence.
Day 2 Outcome
Participants finish Day 2 able to reason through ApplicationSets and App-of-Apps, enforce platform boundaries, and restore stable service during realistic Argo CD incidents.
Recommended Training Environment
Each participant-or pair, if infrastructure is constrained-receives one Linux VM containing:
Two lightweight Kubernetes clusters representing the Argo CD management cluster and a remote workload cluster
A preinstalled but resettable Argo CD deployment
kubectl, helm, Git, and the Argo CD CLI
Access to the Argo CD UI and API
Prepared Git repositories containing Helm, ApplicationSet, and App-of-Apps examples
Reset scripts or snapshots between major labs
This topology reproduces the important management-cluster/workload-cluster relationship without requiring a full Rancher installation per participant. Instructor demonstrations and course diagrams map the lab environment to a production Rancher/RKE2 implementation.



