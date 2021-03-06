// import React from "react";
// import ReactDom from "react-dom";
// import AvatarCropper from 'react-avatar-cropper'

// export default class App extends React.Component{
//   getInitialState = () => {
//     return {
//       cropperOpen: false,
//       img: null,
//       croppedImg: "http://www.fillmurray.com/400/400"
//     };
//   }
  
//   handleFileChange = (dataURI) => {
//     this.setState({
//       img: dataURI,
//       croppedImg: this.state.croppedImg,
//       cropperOpen: true
//     });
//   }

//   handleCrop = (dataURI) => {
//     this.setState({
//       cropperOpen: false,
//       img: null,
//       croppedImg: dataURI
//     });
//   }

//   handleRequestHide = () => {
//     this.setState({
//       cropperOpen: false
//     });
//   }

//   render () {
//     return (
//       <div>
//         <div className="avatar-photo">
//           <FileUpload handleFileChange={this.handleFileChange} />
//           <div className="avatar-edit">
//             <span>Click to Pick Avatar</span>
//             <i className="fa fa-camera"></i>
//           </div>
//           <img src={this.state.croppedImg} />
//         </div>
//         {this.state.cropperOpen &&
//           <AvatarCropper
//             onRequestHide={this.handleRequestHide}
//             cropperOpen={this.state.cropperOpen}
//             onCrop={this.handleCrop}
//             image={this.state.img}
//             width={400}
//             height={400}
//           />
//         }
//       </div>
// 	    );
// 	  }
// 	}
// }