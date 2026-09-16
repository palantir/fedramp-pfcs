# {{ serviceIdentification.serviceName }}

**{{ serviceIdentification.providerName }}**

{{ serviceIdentification.serviceDescription }}

## Offering

| Field | Value |
|---|---|
| Certification | {{ serviceIdentification.certificationType }} |
| FedRAMP ID | {{ serviceIdentification.fedRampPackageId }} |
{% if serviceIdentification.ueiNumber is defined %}
| UEI | {{ serviceIdentification.ueiNumber }} |
{% endif %}
| Service acronym | {{ serviceIdentification.serviceAcronym }} |
| Service model | {{ serviceProperties.serviceType | join(", ") }} |
| Deployment model | {{ serviceProperties.deploymentModel }} |
| Product website | [{{ serviceIdentification.website }}]({{ serviceIdentification.website }}) |

## Business categories

{{ serviceProperties.businessCategory | join(" · ") }}

## Contacts and assessor

| Role | Contact |
|---|---|
{% for contact in contactInformation %}
| {{ contact.contactType }} | {{ contact.contactName }} · [{{ contact.contactEmail }}](mailto:{{ contact.contactEmail }}) |
{% endfor %}
| Independent assessor | {{ assessor.name }} · FedRAMP ID {{ assessor.assessorID }} |

## Certified services

{{ certifiedServices | length }} services are included in this certification. Services not listed here are outside the FedRAMP Minimum Assessment Scope.

| Service | Available | Category |
|---|---|---|
{% for service in certifiedServices | sort(attribute="serviceName") %}
| {{ service.serviceName }} | {{ service.dateAvailable }} | {{ service.securityCategory }} |
{% endfor %}

**About service dates**

> {{ certifiedServicesNote.dateAvailableBasis }}

## Certified service details

{% for service in certifiedServices | sort(attribute="serviceName") %}
### {{ service.serviceName }}

**FIPS 199 {{ service.securityCategory }} · Available since {{ service.dateAvailable }}**

{{ service.serviceDescription }}
{% if service.providerWebsite is defined or service.securityAdminGuideUrl is defined or service.supplementalDocuments is defined %}

{% if service.providerWebsite is defined %}[Provider website]({{ service.providerWebsite }}){% endif %}{% if service.securityAdminGuideUrl is defined %} · [Security administration guide]({{ service.securityAdminGuideUrl }}){% endif %}{% if service.supplementalDocuments is defined %} · [Supplemental documents]({{ service.supplementalDocuments }}){% endif %}
{% endif %}

{% endfor %}
{% if servicesOutsideMinimumAssessmentScope | default([]) %}
## Services outside the minimum assessment scope

{% for service in servicesOutsideMinimumAssessmentScope %}
### {{ service.serviceName }}

{{ service.reason }}

{% if service.supplementalDocuments is defined %}[Supplemental documents]({{ service.supplementalDocuments }}){% endif %}

{% endfor %}
{% endif %}
## Trust Center

| Field | Value |
|---|---|
| Repository | [{{ serviceProperties.trustCenter.url }}]({{ serviceProperties.trustCenter.url }}) |
| Type | {{ serviceProperties.trustCenter.repositoryType | join(", ") }} |
| Description | {{ serviceProperties.trustCenter.repositoryDescription }} |
| Authentication required | {{ "Yes" if serviceProperties.trustCenter.authenticationRequired else "No" }} |
{% if serviceProperties.trustCenter.accessRequestInstructions is defined %}
| Access instructions | {{ serviceProperties.trustCenter.accessRequestInstructions }} |
{% endif %}

## Secure Configuration Guidance

| Field | Value |
|---|---|
| Repository | [{{ serviceProperties.secureConfigurationGuidance.url }}]({{ serviceProperties.secureConfigurationGuidance.url }}) |
| Type | {{ serviceProperties.secureConfigurationGuidance.repositoryType | join(", ") }} |
| Description | {{ serviceProperties.secureConfigurationGuidance.repositoryDescription }} |
| Authentication required | {{ "Yes" if serviceProperties.secureConfigurationGuidance.authenticationRequired else "No" }} |
{% if serviceProperties.secureConfigurationGuidance.accessRequestInstructions is defined %}
| Access instructions | {{ serviceProperties.secureConfigurationGuidance.accessRequestInstructions }} |
{% endif %}

## Continuous monitoring

| Field | Value |
|---|---|
| Next Ongoing Certification Report | {{ serviceProperties.nextOngoingCertificationReportDate }} |
| Next Quarterly Review | {{ serviceProperties.nextQuarterlyReview.date }}, {{ serviceProperties.nextQuarterlyReview.startTime }} |
| Quarterly Review registration | [Request an invitation]({{ serviceProperties.nextQuarterlyReview.registrationUrl }}). {{ serviceProperties.nextQuarterlyReview.registrationInstructions }} |
| OCR feedback and questions | [Email the {{ serviceIdentification.serviceAcronym }} FedRAMP ISSO]({{ serviceProperties.ongoingCertificationReportFeedbackUrl }}). {{ serviceProperties.ongoingCertificationReportFeedbackInstructions }} |

## Certification Data documentation

Statuses describe artifact availability, not certification status.

| Document | Human-readable | Machine-readable | Status |
|---|---|---|---|
{% for item in documentationOverview %}
| {% if item.url is defined %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} ({{ item.rule }}) | {{ item.humanReadable }} | {{ item.machineReadable }} | {{ item.status }} |
{% endfor %}

---

Version {{ metadata.version }} · last updated {{ metadata.lastUpdated }} · source {{ metadata.sourceOfUpdate }} · responsible official {{ metadata.responsibleAccountableOfficial.name }} ({{ metadata.responsibleAccountableOfficial.title }}, [{{ metadata.responsibleAccountableOfficial.email }}](mailto:{{ metadata.responsibleAccountableOfficial.email }})).
