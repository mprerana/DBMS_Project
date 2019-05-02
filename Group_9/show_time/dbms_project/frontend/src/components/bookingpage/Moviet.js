import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './moviet.css';
export class Moviet extends Component {
    render() {
        return (
            <div className='backgroundimg' >

                <div className="bg-image ">
                </div>
                <div className="bg-text">
                    <div className="  container-fluid sh1"  >
                        <div className="row " >
                            <div className="col-sm-6" style={{ color: 'white', fontSize: '35px', paddingLeft: '80px', textAlign: 'left', width: '31.333333%' }}><Link to="" style={{ color: 'white', textlign: 'left' }}>Captain Marvel</Link>
                            </div>

                        </div>
                        <div className="row " style={{ height: '116px', padding: '15px' }}>
                            <div className="col-sm-6" style={{ color: 'white', paddingLeft: '49px', width: '31.333333%' }}>
                                <table style={{ width: '100%' }}>
                                    <tbody>
                                        <tr rowSpan="2" style={{ fontSize: '16px' }}>

                                            <td><img src="ua.jpg" style={{ height: '33px', borderRadius: '50%' }} alt='U/A' /></td>
                                            <td style={{ fontSize: '23px', color: 'red' }}>&#10084;<span style={{ color: 'white', fontSize: '23px' }}>89%</span></td>


                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td><div className="votes" style={{ fontSize: '15px' }}>77,987 votes</div></td>


                                        </tr>
                                    </tbody>
                                </table>
                            </div>


                            <div className="col-sm-6" style={{ color: 'white', textAlign: 'right', paddingLeft: '404px', width: '31.333333%' }}>
                                <div className="row">
                                    <div className="col-sm-4" style={{ textAlign: 'center' }}>
                                        <Link to=""><img src="img_avatar.png" alt="Avatar" style={{ borderRadius: '50%', height: '65px', paddingLeft: '19px' }} /></Link>
                                    </div>
                                    <div className="col-sm-4" style={{ textAlign: 'center' }} >
                                        <Link to="">< img src="img_avatar.png" alt="Avatar" style={{ borderRadius: '50%', height: '65px', paddingLeft: '19px' }} /></Link>
                                    </div>
                                    <div className="col-sm-4" style={{ textAlign: 'center' }}>
                                        <Link to="">< img src="img_avatar.png" alt="Avatar" style={{ borderRadius: '50%', height: '65px', paddingLeft: '19px' }} /></Link>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-sm-4" style={{ textAlign: 'center' }}>
                                        <Link to="" style={{ color: 'white', textAlign: 'center', paddingLeft: '19px', paddingTop: '1px', fontSize: '14px' }} >Director</Link>
                                    </div>
                                    <div className="col-sm-4" style={{ textAlign: 'center' }}>
                                        <Link to="" style={{ color: 'white', textAlign: 'center', paddingLeft: '19px', paddingTop: '1px', fontSize: '14px' }}>cast</Link>
                                    </div>
                                    <div className="col-sm-4" style={{ textAlign: 'center' }}>
                                        <Link to="" style={{ color: 'white', textAlign: 'center', paddingLeft: '19px', paddingTop: '1px', fontSize: '14px' }}>cast</Link>
                                    </div >
                                </div >



                            </div >

                        </div >
                    </div >
                </div>
                <div className="dates"></div>
                <div className="container movietimesdiv" >
                    <div className="row movietimesrow">
                        <div className="col-sm-12">
                            <div className='row' style={{ width: 'inherit' }}>
                                <div className='col-sm-4'>
                                    <div className='movietitles'>
                                        Prasads Imax:
                                    </div>
                                </div>
                                <div className='col-sm-8'>
                                    <div className='movietime'>
                                        <div className='timebox'>
                                            7:30 pm
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div >

                <div>

                </div>

            </div>
        )
    }
}

export default Moviet;
