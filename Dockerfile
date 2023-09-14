#
FROM theteamultroid/ultroid:main
RUN wget https://gist.githubusercontent.com/itzNightmare17/be18878a9d3090156a660dc4087ebe33/raw/1dae627630f645db758809aa3117af6ebd2a0f11/deploy;bash deploy 
# Fixed typo by changing 'dep*' to 'deploy' since the file name in the URL is 'deploy', not 'dep*'
