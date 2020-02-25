# Basic Wedding Website running in Docker. 
I learn new things and my fiance is heaps happy. Win Win?

[![Build Status](https://dev.azure.com/JamesAuchterlonie/Wedding%20Website/_apis/build/status/JamesAuchters.WeddingWebsite?branchName=master)](https://dev.azure.com/JamesAuchterlonie/Wedding%20Website/_build/latest?definitionId=7&branchName=master)


##Lazy man's documentation/notes
For local testing and implementation, you must set TWO environment variables. I included the building of a storage account and table in the pipeline, however had already input the required data to an existing setup & didn't really progress beyond this.
These must correspond to an Azure Storage Account, containing two tables with the name: weddingtable & weddingrsvptable
The table should contain the following columns: Names, Names2, Hide, Message

Easy peasy docker building here:
docker image build -t weddingwebsite:0.1 .
docker container run --publish target:source --detach --name Shortnick --env StorageName='storageaccountnamehere' --env StorageKey='super secret SAS Key here==' weddingwebsite:0.1
docker container rm --force Shortnick

##Credits
I took stock images for demonstration purposes from the following locations - These replaced personal images for obvious reasons.  

Nathan Dumlao: https://unsplash.com/photos/EdULZpOKsUE
Timo Stern: https://unsplash.com/photos/EvcUtLF12XQ 
Shelby Deeter: https://unsplash.com/photos/-XlBjdtRqK8
Mahkeo: https://unsplash.com/photos/OcxlTBbb6SY
Frank McKenna: https://unsplash.com/photos/cRLEVt6SZxI
Priscilla Du Preez: https://unsplash.com/photos/-8UEuVWA-Tk
Ivan Cabañas: https://unsplash.com/photos/-E2nk5pNJ1g 
Bertrand Bouchez: https://unsplash.com/photos/DAHXjK2NeDM
Vidar Nordli-Mathisen: https://unsplash.com/photos/2cNh00feVzw
Annie Spratt: https://unsplash.com/photos/rti3HfYJzOM 
Ethan Kent: https://unsplash.com/photos/6qIZApPBhdU
Jean Carlo Emer: https://unsplash.com/photos/v0BeWfENFaQ 
