import React from 'react'
import AppBar from 'material-ui/AppBar'
//import {Toolbar, ToolbarGroup, ToolbarSeparator, ToolbarTitle} from 'material-ui/Toolbar'
import FlatButton from 'material-ui/FlatButton'
import {Link} from 'react-router-dom'
import {white,indigo500} from 'material-ui/styles/colors'
// import senselogo from '../../assets/image/sense-health-logo.png'
// import Avatar from 'material-ui/Avatar'

import notifications from '../../assets/stylesheets/icons/notifications_24px.svg';
import dashboard from '../../assets/stylesheets/icons/dashboard_24px.svg';
import book from '../../assets/stylesheets/icons/book_24px.svg';
import account_circle from '../../assets/stylesheets/icons/account_circle_24px.svg';

export default class Header extends React.Component{

	render(){
		const style = {
			appBar: {
				position: 'fixed',
				backgroundColor: '#C2A060',
				overflow:'hidden',
				width:'100%',
				maxHeight: 57,
				alignText:'center'
			}
		}

		return(
			<div>
				<div id="general-navwrapper">
				  	<div id="general-navbar">
	  					<ul id="general-navbar-ul">
		  					<div className="general-title">
		  						<label style={{fontFamily: 'lb_constantia', fontSize: 35}}>Liteboard</label>
		  					</div>
							<div className="general-navbar-icons">
								<a className="svg-icon"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg></a>
								<a className="svg-icon"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg></a>
								<a className="svg-icon"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg></a>
								<a className="svg-icon"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg></a>
							</div>
						</ul>				 
				  	</div>
				</div>
			</div>
		)
	}
}