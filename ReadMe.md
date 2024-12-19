## Postrank Algorithm

This is a simple algorithm that is used to find nearby locations like a delivery hub, post office, or some other service hub for any given location ```x```. Could be exteneded to any databases like SQL, PostGRES, or Pandas' Dataframe.

Here's is the Algorithm: 

```
Step 1: Read the Destination Address
Step 2: Convert the Address to Longitude and Latitude using the API of your choice. (Google Maps or GeoPandas or MapMyIndia)
Step 3: Find Nearby Locations(Service Hubs) using the Haversine Formula

```
Examples: 

### - Find Nearby PostOffices

x : Amarajyothi Hospital, Kamalapur Road, Dharwad, Karnataka

output: Returns the valid PinCode for the area and returns the nearest post offices to ```x``` and its details!

![PostOffice_Output](PostOffice_out.PNG)



### - Find Nearby Delivery Hubs

x : Bapat Galli. Belgaum, Karnataka

output: Returns all delivery hubs near that area and returns the nearest delivery bubs to ```x``` and its details!

![PostOffice_Output](PostOffice_out.PNG)