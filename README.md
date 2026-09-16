# Palantir Federal Cloud Service

**Palantir Technologies Inc.**

The Palantir Federal Cloud Service (PFCS) is a dedicated environment for the purpose of delivering Palantir software to federal government customers as a cloud service. Palantir software, including Foundry, AIP, Gotham, Apollo, and supporting products utilizing the same infrastructure, enables a multitude of collaborative and operational workflows for end government users. Palantir enables organizations to take advantage of best-in-class Artificial Intelligence, Machine Learning, Data Integration, Data Storage, Data Processing, Analytics, Visualization, Operations, Cybersecurity, and Software Deployment capabilities. The PFCS allows customers to acquire Palantir to quickly deliver value against their hardest problems. PFCS includes deployments on AWS GovCloud, Azure Government, Azure Commercial, Google Cloud Platform (GCP), and AWS US East/West. PFCS deployments on AWS US East/West are limited to Moderate workloads because AWS US East/West holds only a FedRAMP Moderate authorization. PFCS combines the formerly separated PFCS High (FR2434554673) and PFCS Moderate (FR1912671248) packages.

## Offering

| Field | Value |
|---|---|
| Certification | Rev5 |
| FedRAMP ID | FR2434554673 |
| UEI | FSY4LVSBGWB7 |
| Service acronym | PFCS |
| Service model | PaaS, SaaS |
| Deployment model | Public Cloud |
| Product website | [https://www.palantir.com/](https://www.palantir.com/) |

## Business categories

Analytics · Collaboration · Cybersecurity & Risk Management · Data Management · Development Tools · Finance · Fleet Management · Law Enforcement · Operations Management · Research

## Contacts and assessor

| Role | Contact |
|---|---|
| Security | FedRAMP ISSO · [fedramp-isso@palantir.com](mailto:fedramp-isso@palantir.com) |
| Sales | Palantir Federal Sales · [fedramp@palantir.com](mailto:fedramp@palantir.com) |
| Independent assessor | Schellman Compliance, LLC · FedRAMP ID 136571 |

## Certified services

7 services are included in this certification. Services not listed here are outside the FedRAMP Minimum Assessment Scope.

| Service | Available | Category |
|---|---|---|
| AIP | 2023-04-07 | High |
| Apollo | 2019-12-18 | High |
| Apollo Agent | 2019-12-18 | High |
| Foundry | 2019-12-18 | High |
| Gotham | 2019-12-18 | High |
| Gotham Thick Client | 2019-12-18 | High |
| Palantir Data Connector | 2019-12-18 | High |

**About service dates**

> dateAvailable identifies when each service was available in PFCS or entered a predecessor PFCS authorization package; it is not the date of the current FedRAMP High certification. PFCS first received FedRAMP Moderate authorization on 2019-12-18 under FR1912671248 and was later certified at the High baseline on 2024-11-19 under FR2434554673. PFCS now combines the formerly separate Moderate and High packages. AIP's dateAvailable is its 2023-04-07 public announcement date. The remaining services use the initial PFCS Moderate authorization date based on provider-supplied package history.

## Certified service details

### AIP

**FIPS 199 High · Available since 2023-04-07**

Palantir's Artificial Intelligence Platform (AIP) connects large language models (LLMs) and other AI technologies with customer data and operations within PFCS. AIP provides unified access to a range of open-source, self-hosted, and commercial LLMs through the AIP Model Catalog, and supports customer-connected models through its Bring Your Own Model capability. AIP includes tools for building, deploying, and managing models throughout their lifecycle, with LLM capacity management controls that allow administrators to govern model availability and resource consumption. The platform facilitates the conversion of LLM logic flows into secure, governed automations, with support for staging ontology edits for human review, while end-to-end traceability ensures rigorous auditing of all automation execution and downstream effects.

### Apollo

**FIPS 199 High · Available since 2019-12-18**

Apollo is Palantir's continuous delivery and operations platform, providing a single control layer to deploy, upgrade, monitor, and manage software both for Palantir for PFCS and customers using Apollo to deploy their own applications. Apollo uses a Hub-and-Spoke architecture in which a central Hub environment orchestrates deployments to Spoke environments through an Orchestration Engine. Apollo manages the full deployment lifecycle, including release channel promotion pipelines, ramped rollouts, automated rollbacks, maintenance windows, and bulk release recalls, across cloud, on-premises, and disconnected or air-gapped environments. Apollo also provides real-time vulnerability scanning with SBOM and CVE visibility into deployed services.

### Apollo Agent

**FIPS 199 High · Available since 2019-12-18**

Apollo upgrades components via a local agent which regularly queries the Apollo server to determine if any updates or configuration changes are available. Apollo maintains a catalog of versions of services from the artifact repository and is informed of the current state of service installations by agents running alongside those installations. Apollo applies upgrades subject to defined rules, automatically adjudicates releases by observing performance metrics and error states, and gradually rolls out releases that pass adjudication. Apollo Agent is used with the Apollo application.

### Foundry

**FIPS 199 High · Available since 2019-12-18**

Foundry is Palantir's data operations platform, providing a unified environment for data connectivity and integration, pipeline development, ontology building, analytics, model development, and application delivery. Foundry ingests and integrates data from diverse sources and formats, transforming it through automated pipelines into a semantic data layer known as the Ontology. Foundry enforces security and governance as an integrated layer across all platform capabilities, with access controls managed through organizations, spaces, projects, roles, users, groups, and markings, and maintains comprehensive audit logging and data lineage tracking across all operations.

### Gotham

**FIPS 199 High · Available since 2019-12-18**

Gotham is Palantir's platform for intelligence analysis, investigative operations, and mission planning. It integrates structured and unstructured data from disparate sources into a unified data asset built on a dynamic ontology of entities, properties, and relationships. Gotham provides an integrated workspace for geospatial mapping, network analysis, and temporal pattern detection, supporting the complete operational lifecycle from intelligence collection and production through mission planning, execution, and after-action review. Every piece of data ingested is tethered to its original source with traceable lineage, and all user and administrator interactions are recorded in audit logs.

### Gotham Thick Client

**FIPS 199 High · Available since 2019-12-18**

Palantir Gotham's Titanium is the workspace for Intel-Ops fusion. Palantir Gotham integrates, enhances, and fuses data from many systems to enable decision making at every echelon and in every domain. Thick clients can be rolled out either through central infrastructure of the customer, or via a download from the Gotham landing page's Palantir Global Launcher link. Gotham Thick Client (Titanium) is used with the Gotham application.

### Palantir Data Connector

**FIPS 199 High · Available since 2019-12-18**

The Foundry Data Connector supports connection with all types of source systems, structured or unstructured, and supports batch, micro-batch, or streaming. It supports on-premises and cloud-based sources, including edge devices. Users can customize syncs with querying parameters, retries, and time- or trigger-based schedules, and can monitor sync performance for tuning and latency of data ingestion. Palantir Data Connector is used with Foundry and Gotham applications.

## Trust Center

| Field | Value |
|---|---|
| Repository | [https://pfcsdocs.palantirgov.com/](https://pfcsdocs.palantirgov.com/) |
| Type | Trust Center |
| Description | PFCS Documentation Repository. Access is restricted to verified federal government accounts and to FedRAMP Recognized independent assessment services supporting an assessment of this offering. |
| Authentication required | Yes |
| Access instructions | Federal agencies and FedRAMP Recognized independent assessment services request access by contacting FedRAMP-ISSO@palantir.com with the requesting organization, the point of contact to be provisioned, and the authorization or assessment activity the access supports. Access persists for the duration of that activity; parties do not submit a new request for each document. |

## Secure Configuration Guidance

| Field | Value |
|---|---|
| Repository | [https://www.palantir.com/docs](https://www.palantir.com/docs) |
| Type | Secure Configuration Guidance |
| Description | Recommended secure configuration guidance for PFCS, covering secure access, configuration, operation and decommissioning of top-level administrative accounts and the security settings operable only by those accounts. |
| Authentication required | No |

## Continuous monitoring

| Field | Value |
|---|---|
| Next Ongoing Certification Report | 2026-09-22 |
| Next Quarterly Review | 2026-10-28, 13:30:00-04:00 |
| Quarterly Review registration | [Request an invitation](mailto:FedRAMP-ISSO@palantir.com?subject=PFCS%20Quarterly%20Review%20registration). Request an invitation by email to FedRAMP-ISSO@palantir.com. |
| OCR feedback and questions | [Email the PFCS FedRAMP ISSO](mailto:FedRAMP-ISSO@palantir.com?subject=PFCS%20Ongoing%20Certification%20Report%20feedback). Send feedback or questions about any Ongoing Certification Report by email to FedRAMP-ISSO@palantir.com. Questions and answers are published, anonymized and desensitized, in the Feedback Summary of a subsequent report. |

## Certification Data documentation

Statuses describe artifact availability, not certification status.

| Document | Human-readable | Machine-readable | Status |
|---|---|---|---|
| Public offering information (CDS-CSO-PUB) | Required | Required | In development |
| [Certification Package Overview](https://pfcsdocs.palantirgov.com/) (CPO-CSO-OVR) | Required | Required | In development |
| [Security Decision Record](https://pfcsdocs.palantirgov.com/) (SDR-CSO-FRR) | Required | Required | In development |
| [Ongoing Certification Report](https://pfcsdocs.palantirgov.com/) (CCM-OCR-AVL) | Required | Required | In development |
| [Vulnerability Detail Report](https://pfcsdocs.palantirgov.com/) (VER-RPT-PER) | Required | Required | In development |
| [Accepted Vulnerability Information](https://pfcsdocs.palantirgov.com/) (VER-RPT-AVI) | Required | Required | In development |
| [Significant Change Notifications](https://pfcsdocs.palantirgov.com/) (SCN-CSO-HRM) | Required | Required | In development |
| [Incident Reports](https://pfcsdocs.palantirgov.com/) (IEC-CSO-IIR) | Required | Required | In development |
| [Policy and procedure index](https://pfcsdocs.palantirgov.com/) (CDS-CSO-IRP) | Required | Required | In development |
| Service availability (CDS-CSO-AVR) | Required | Required | In development |
| [Per-service certification materials](https://pfcsdocs.palantirgov.com/) (CDS-CSO-PSM) | Required | Required | In development |
| [FedRAMP Certification Reports](https://pfcsdocs.palantirgov.com/) (CDS-CSO-FRC) | Required | Not applicable | Conditional |
| [Historical Certification Data snapshots](https://pfcsdocs.palantirgov.com/) (CDS-CSO-HAD) | Required | Required | In development |
| [Secure Configuration Guidance](https://www.palantir.com/docs) (SCG-CSO-RSC) | Required | Not required (SCG-ENH-MRG is a SHOULD) | Published |

---

Version 1.0.0 · last updated 2026-09-15T00:00:00-06:00 · source validation-preview · responsible official PFCS and PFCS-SS ISSO (Information System Security Officer, [FedRAMP-ISSO@palantir.com](mailto:FedRAMP-ISSO@palantir.com)).
