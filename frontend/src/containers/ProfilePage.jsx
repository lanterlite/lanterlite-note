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
import AvatarCropper from 'react-avatar-cropper'
// import { Cropper } from 'react-image-cropper'
// import Croppie from 'react-croppie'
import Paper from 'material-ui/Paper'
import Breadcrumb from 'react-breadcrumb';
import BaseContainer from '../containers/BaseContainer';
import profileImage from '../assets/dummy/profile-image.jpg'
// import ReactCrop from 'react-image-crop';
// import 'react-image-crop/lib/ReactCrop.scss';
import Cropper from 'react-cropper';
import 'cropperjs/dist/cropper.css';


var Base64 = {
    characters: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" ,

    encode: function( string )
    {
        var characters = Base64.characters;
        var result     = '';

        var i = 0;
        do {
            var a = string.charCodeAt(i++);
            var b = string.charCodeAt(i++);
            var c = string.charCodeAt(i++);

            a = a ? a : 0;
            b = b ? b : 0;
            c = c ? c : 0;

            var b1 = ( a >> 2 ) & 0x3F;
            var b2 = ( ( a & 0x3 ) << 4 ) | ( ( b >> 4 ) & 0xF );
            var b3 = ( ( b & 0xF ) << 2 ) | ( ( c >> 6 ) & 0x3 );
            var b4 = c & 0x3F;

            if( ! b ) {
                b3 = b4 = 64;
            } else if( ! c ) {
                b4 = 64;
            }

            result += Base64.characters.charAt( b1 ) + Base64.characters.charAt( b2 ) + Base64.characters.charAt( b3 ) + Base64.characters.charAt( b4 );

        } while ( i < string.length );

        return result;
    } ,

    decode: function( string )
    {
        var characters = Base64.characters;
        var result     = '';

        var i = 0;
        do {
            var b1 = Base64.characters.indexOf( string.charAt(i++) );
            var b2 = Base64.characters.indexOf( string.charAt(i++) );
            var b3 = Base64.characters.indexOf( string.charAt(i++) );
            var b4 = Base64.characters.indexOf( string.charAt(i++) );

            var a = ( ( b1 & 0x3F ) << 2 ) | ( ( b2 >> 4 ) & 0x3 );
            var b = ( ( b2 & 0xF  ) << 4 ) | ( ( b3 >> 2 ) & 0xF );
            var c = ( ( b3 & 0x3  ) << 6 ) | ( b4 & 0x3F );

            result += String.fromCharCode(a) + (b?String.fromCharCode(b):'') + (c?String.fromCharCode(c):'');

        } while( i < string.length );

        return result;
    }
};

export default class LoginPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            user: [],
            files: [],
            isEmailDisabled: true,
            editButtonValue: "Edit",
            isChangePassword: false,
            profileImageUrl: 'http://localhost:3000/profile_picture/profile-image.jpg',
            newProfileImageUrl: null,
            isDialogOpen: false,

            cropperOpen: false,
            img: null,
            croppedImg: "http://www.fillmurray.com/400/400"
        };
    }
	
    /**
     * Get all master data from server
     */
    getData = () => {
        const self = this
        var url = this.props.url.site + this.props.url.backendRoute.version + this.props.url.backendRoute.user + '/1'
        axios.get(url).then(function(request){
            let stateCopy = Object.assign({}, self)
            stateCopy.state.user = request.data
            self.setState({ stateCopy })
            self.getImage()
        })
    }

	componentWillMount = () => {
		document.body.style.backgroundColor = "#FFFCC9";
        this.getData()
	}
	
    validatePassword = () => {
        if (this.state.isChangePassword === true){
            // code here
            return true
        }
        else
            return true
    }

    onSave = () => {
        const self = this
        if (
            this.validateAlphanumeric(self.state.user.username) &&
            this.validateEmail(self.state.user.email) &&
            this.validatePassword()
        ){
            var data = [];

            var obj = {
                id              : self.state.user.id              || "",
                name            : self.state.user.name            || "",
                email           : self.state.user.email           || "",
                password        : self.state.user.password        || "",
                username        : self.state.user.username        || "",
                image           : self.state.user.image           || "",
                friendlist      : self.state.user.friendlist      || null,
                is_activated    : self.state.user.is_activated    || false,
                created_at      : self.state.user.created_at      || "",
                updated_at      : self.state.user.updated_at      || "",
                violation_id    : self.state.user.violation_id    || null,
            }
            data.push(obj)

            axios({
                url: self.props.url.site + self.props.url.backendRoute.version + self.props.url.backendRoute.user,
                method: 'put',
                data: data
            })
            .then(function (response) {
            })
            .catch(function (error) {
            })                        
        }
    }

    onEdit = () => {
        let stateCopy = Object.assign({}, this)
        if (stateCopy.state.isEmailDisabled === true) {
            stateCopy.state.isEmailDisabled = false
            stateCopy.state.editButtonValue = 'Done'
        }
        else {
            stateCopy.state.isEmailDisabled = true
            stateCopy.state.editButtonValue = 'Edit'
        }
        this.setState({ stateCopy })
    }

    onChangePassword = () => {
        let stateCopy = Object.assign({}, this)
        if (stateCopy.state.isChangePassword === false) {
            stateCopy.state.isChangePassword = true
            this.setState({ stateCopy })
        }
    }

    validateEmail = (email) =>{  
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){  
            return (true)  
        }
        else{
            alert("You have entered an invalid email address!")  
            return (false)  
        }
    }

    validateAlphanumeric = (value) => {  
        var letterNumber = /^[0-9a-zA-Z]+$/;  
        if ( value.match(letterNumber) ) {  
            return true;
        }  
        else {
            alert("username must only letter A-Z and number 0-9");   
            return false;   
        }  
    }

    onDrop = (files) => {
        console.log(files[0].preview)
        var stateCopy = Object.assign({}, this)
        stateCopy.state.isDialogOpen = true
        stateCopy.state.files = files[0]
        stateCopy.state.newProfileImageUrl = files[0].preview
        this.setState({ stateCopy })
        console.log(this.state.isDialogOpen)
    }


    onCloseDialog = () => {
        var stateCopy = Object.assign({}, this)
        stateCopy.state.isDialogOpen = false
        this.setState({ stateCopy });
    }

    dataURItoBlob = (dataURI) => {
        // convert base64/URLEncoded data component to raw binary data held in a string
        var byteString;
        if (dataURI.split(',')[0].indexOf('base64') >= 0)
            byteString = atob(dataURI.split(',')[1]);
        else
            byteString = unescape(dataURI.split(',')[1]);

        // separate out the mime component
        var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

        // write the bytes of the string to a typed array
        var ia = new Uint8Array(byteString.length);
        for (var i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }

        return new Blob([ia], {type:mimeString});
    }

    onUploadDialog = () => {
        const dataUrl = this.refs.cropper.getCroppedCanvas().toDataURL();

        var blob = this.dataURItoBlob(dataUrl)

        const self = this
        var data = new FormData()
        var imagedata = blob
        data.append('data', imagedata)
        axios({
            url: this.props.url.site + this.props.url.backendRoute.version + this.props.url.backendRoute.user + '/upload/',
            method: 'post',
            data: data,
            headers: {
                'Accept': 'application/json',
                'id': this.state.user.id,
                'created_at': this.state.user.created_at,
            },
        })
        .then(function(response) {
            console.log(response.data)
            self.getData()
            self.onCloseDialog()
        }).catch(function (error) {
            console.log(error)
            self.onCloseDialog()
        })
    }

    getImage = () => {
        var self = this
        axios({
            url: this.props.url.site + this.props.url.backendRoute.version + this.props.url.backendRoute.user + '/image/',
            method: 'put',
            headers: {
                'Accept': 'application/json',
                'id': this.state.user.id,
                'filename': this.state.user.image,
                'created_at': this.state.user.created_at,
            },
        })
        .then(function(request){
            var stateCopy = Object.assign({}, self)
            stateCopy.state.profileImageUrl = request.data
            self.setState({ stateCopy })
        })
        .catch(function (error) {
            console.log(error)
        })     
    }

    onSendEmail = () => {
        window.open('mailto:test@example.com?subject=subject&body=body');
    }

    render(){
        let dropzoneRef;

        const dropImageAction = [
            <FlatButton
                label="Upload"
                primary={true}
                onClick={this.onUploadDialog}
            />,
            <FlatButton
                label="Close"
                secondary={true}
                onClick={this.onCloseDialog}
            />,
        ]
        var crop = {
          x: 20,
          y: 10,
          width: 30,
          height: 10
        }
 
		return(
			<div>
				<BaseContainer />
				<div id="body-navwrapper">
				  <div id="body-navbar">
					<div className="profile-paper">
                        <div className="title">
                            <label style={{fontFamily: 'lb_constantia'}} >User Account</label>
                        </div>
                            <input 
                                id="brown-button"
                                type="button" 
                                value="Save"
                                onClick={this.onSendEmail}
                            /> 
                        {/* UPLOAD PHOTO */}
                        <Dropzone style={{ display: 'none' }}ref={(node) => { dropzoneRef = node; }} onDrop={this.onDrop}>
                            <p>Drop files here.</p>
                        </Dropzone>
                        <Dialog
                            actions={dropImageAction}
                            open={this.state.isDialogOpen}
                            // style={{ width: '50%', height: '50%' }}
                        >
                            <div style={{ textAlign: 'center' }} >
                                   <div style={{ margin: 'auto auto', align:'center' }}>
                                   <Cropper
                                    ref='cropper'
                                    src={this.state.newProfileImageUrl}
                                    style={{ margin: 'auto auto', align:'center', height: '200px', width: '200px'}}
                                    // Cropper.js options 
                                    aspectRatio={1 / 1}
                                    guides={true}
                                    backgroundColor={true}
                                    viewMode={3}
                                    />
                                    </div>
                                    </div>
                                   {/*
                                <ReactCrop src={this.state.newProfileImageUrl} crop={crop} />
                                <ul style={{ listStyle: 'none' }}>
                                    <li><img alt="User Profile" style={{ textAlign: 'center' }} id="profile-photo" src={this.state.newProfileImageUrl} /></li>
                                    <li style={{ marginTop: '10px' }}><label>Wanna change your profile picture with this picture?</label></li>
                                </ul>
                                    */}
                        </Dialog>
                        <div className="profile-photo">
                            <ul style={{ listStyle: 'none' }}>
                                <li> <img alt="User Profile" id="profile-photo" src={this.state.profileImageUrl} /></li> 
                                <li style={{ marginTop: '10px' }}><button id="brown-button" type="button" onClick={() => { dropzoneRef.open() }}> Change Picture </button></li>
                            </ul>
                        </div>

                        <form className="profile-fields">
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Username:</label> 
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="text-box" type="text" 
                                    value={this.state.user.username}
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.username = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                            </div>
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Name:</label>
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="text-box" 
                                    type="text" 
                                    value={this.state.user.name}
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.name = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                            </div>
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Email:</label>
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="text-box" 
                                    type="text" 
                                    disabled={this.state.isEmailDisabled}
                                    value={this.state.user.email}
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.email = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                                <input 
                                    type="button" 
                                    className="edit-button"
                                    value={this.state.editButtonValue}
                                    onClick={this.onEdit}
                                />
                            </div>
                            {this.state.isChangePassword === true?
                                <div className="list">
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="password-text-box" 
                                    type="text" 
                                    value=""
                                    placeholder="Old Password"
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.email = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                                </div>
                                :
                                <div className="list">
                                <a
                                    style={{fontFamily: 'lb_constantia'}} 
                                    onClick={this.onChangePassword}
                                    className="change-password"
                                >Change Password</a>
                                </div>
                            }
                            {this.state.isChangePassword === true?

                                <div className="list">
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="password-text-box" 
                                    type="text" 
                                    value=""
                                    placeholder="New Password"
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.email = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                                </div>
                                : null
                            }

                            {this.state.isChangePassword === true?
                                <div className="list">
                                <input 
                                    style={{fontFamily: 'lb_constantia'}} 
                                    className="password-text-box" 
                                    type="text" 
                                    value=""
                                    placeholder="Confirm New Password"
                                    onChange={(e) => { 
                                        let stateCopy = Object.assign({}, this)
                                        stateCopy.state.user.email = e.target.value
                                        this.setState({ stateCopy }) 
                                    }}
                                />
                                </div>
                                : null
                            }
                            <input 
                                id="brown-button"
                                type="button" 
                                value="Save"
                                onClick={this.onSave}
                            /> 
                        </form>
					</div>
				  </div>
				  </div>
		  </div>
        );
    }
}
