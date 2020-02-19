# Portfolio-Website-using-Django
A portfolio website using Django framework


# Hosting on AWS

## Launching an EC2 instance

## Setting up the EC2 instance

## Testing django local server

## Apache Server Configurations

## Final Wrap




# Associate Namecheap or any domain to AWS
1. Login into your AWS console.
2. Go to your instance page.
3. open Elastic Ip which should be under Network and Security in the right menu.
4. click on "Allocate new address button"(orange button).
5. Select the new address created and click “Associate address”.
6. Select your network interface from the drop-down menu.
7. Select private address from the drop-down and click “Associate”.
8. Public Ip address of your EC2 should have changed till now.
9. Please update public Ip in your server too, if you have put it in allowed hosts.
### For other domain name registrar services.
10. Now go back to your domain registering service and open console.
11. find Advance DNS option of your domain name.
12. There should be 2 options under host record, CNAME and A record or @ and www values.
13. In row with "@" symbol, set type to "A Record" and value to your public Ip address of EC2 Instance. Set TTL as per your need.
14. In row with "www" symbol, set type to "CNAME Record" and value to your public DNS of EC2 Instance. Set TTL as per your need.
15. Apply your changes.


### For NameCheap
10. Go to NameCheap Dashboard.
11. Go to Domain List, select your domain and click manage.
12. Click "Advance DNS".
13. Under Host records section there should be two rows with multiple fields.
14. In row with "@" symbol, set type to "A Record" and value to your public Ip address of EC2 Instance. Set TTL as per your need.
15. In row with "www" symbol, set type to "CNAME Record" and value to your public DNS of EC2 Instance. Set TTL as per your need.
16. Apply your changes.

##### You might have to wait for few minutes before association takes place.
