import React from 'react';
//---------------------importing components needed in page---------------------

//--------------------importing material-ui components
import FlatButton from 'material-ui/FlatButton';
import {Link} from 'react-router-dom';
import RaisedButton from 'material-ui/RaisedButton';
import Card from 'material-ui/Card';
import TextField from 'material-ui/TextField';
import Dialog from 'material-ui/Dialog';
//-----------------------importing icon-----------------
import Edit from 'material-ui/svg-icons/editor/mode-edit';
import Done from 'material-ui/svg-icons/action/done';
import Delete from 'material-ui/svg-icons/action/delete';
import Upload from 'material-ui/svg-icons/file/file-upload';
import Back from 'material-ui/svg-icons/navigation/chevron-left';
//------import dropzone for uploading file ----------------
import Dropzone from 'react-dropzone';
import axios from 'axios';
import { Redirect } from 'react-router'
import Paper from 'material-ui/Paper'
import Breadcrumb from 'react-breadcrumb';

export default class LoginPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            user: {
				user_id 			    : props.user.user_id,
                user_email 			    : props.user.user_email,
                user_username 		    : props.user.user_username,
                user_password 		    : props.user.user_password,
                user_profile_pict 	    : props.user.user_profile_pict,
                user_first_name 	    : props.user.user_first_name,
                user_last_name 	        : props.user.user_last_name,
                user_friends 		    : props.user.user_friends,
                user_is_activated 	    : props.user.user_is_activated,
                user_created_at 	    : props.user.user_created_at,
                user_updated_at 	    : props.user.user_updated_at,
                confirm_user_password   : ''
            },
            settings:{
                showEditButton: true,
                showDoneButton: false,
                disableEditText: false,
                isRedirect: false,
            },
            deleteState:{
                openDialog: false,
            },
            uploadState:{
                openDialog:false,
                uploadedFile: null,
				isUploaded: false,
            },
            saveState:{
                openDialog: false,
            },
      };
    }
	
	componentWillMount = () => {
		document.body.style.backgroundColor = "#FFFCC9";
	}

	handleLoginBtnClick = () => {
		console.log(this.state.user)
	}
	
    render(){
		return(
			<div className="profilepage">
				<Card className ="formcontainer">
					<div className ="login-form-base">
						<TextField
							name="user_first_name"
							// style={styles.textStyle}
							readOnly = {this.state.settings.disableEditText}
							value={this.state.user.first_name}
							floatingLabelText="First Name"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									user_first_name:newValue
								}})}
						/>
						<TextField
							name="user_last_name"
							// style={styles.textStyle}
							readOnly = {this.state.settings.disableEditText}
							value={this.state.user.last_name}
							floatingLabelText="Last Name"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									user_last_name:newValue
								}})}
						/>
						<TextField
							name="user_username"
							// style={styles.textStyle}
							readOnly = {this.state.settings.disableEditText}
							value={this.state.user.last_name}
							floatingLabelText="Username"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									user_username:newValue
								}})}
						/>
						<TextField
							name="user_email"
							// style={styles.textStyle}
							readOnly={this.state.settings.disableEditText}
							value={this.state.user.user_email}
							floatingLabelText="Email"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									user_email:newValue
								}})}
						/>
						<TextField
							name="user_password"
							// style={styles.textStyle}
							readOnly={this.state.settings.disableEditText}
							value={this.state.user.user_password}
							floatingLabelText="Password"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									user_password:newValue
								}})}
						/>
						<TextField
							name="confirm_user_password"
							// style={styles.textStyle}
							readOnly={this.state.settings.disableEditText}
							value={this.state.user.user_pconfirm_user_passwordassword}
							floatingLabelText="Confirm Password"
							floatingLabelFixed={true}
							onChange = {(event,newValue) => this.setState({
								user: {
									...this.state.user,
									confirm_user_password:newValue
								}})}
						/><br/>
						<RaisedButton
							label="Login"
							backgroundColor='#C2A060'
							labelColor='#ffffff'
							onClick={this.handleLoginBtnClick}
							// style={styles.reuploadbtn}
							labelPosition="before"
							// icon={<Upload />}
						/>                
					</div>
				</Card>
			</div>
        );
    }
}
