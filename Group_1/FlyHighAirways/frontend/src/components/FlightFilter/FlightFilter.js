import React from 'react';

import { Radio, Checkbox, Divider } from 'antd';

import classes from './FlightFilter.module.css';

const RadioGroup = Radio.Group;

const flightFilter = (props) => {

    console.log();

    return (  
        <div className={classes.FilterColumn}>
            <div className={classes.FlightType}>
                <h2 className={classes.TypeHeader}>Flight Type</h2>
                <RadioGroup 
                    className={classes.FlightOptions} 
                    value={props.filterInfo.flightType}
                    onChange={(e) => props.flightStopType(e)}
                >
                    
                    <Radio value={1}>Non-Stop</Radio><br />
                    <Radio value={2}>Stop</Radio><br />
                    <Radio value={3}>All</Radio>
                </RadioGroup>            
            </div>

            <Divider />

            <div className={classes.FlightType}>
                <h2 className={classes.TypeHeader}>Price Range</h2>

                <RadioGroup 
                    className={classes.FlightOptions} 
                    value={props.filterInfo.priceRange}
                    onChange={e => props.flightPriceType(e)}
                >
                    
                    <Radio value={3000}>
                        <span>&lt; 3000</span>
                    </Radio>
                    <br />
                    
                    <Radio value={5000}>
                        <span>&lt; 5000</span>
                    </Radio>
                    <br />

                    <Radio value={7000}>
                        <span>&lt; 7000</span>
                    </Radio>
                    <br />

                    <Radio value={9000}>
                        <span>&gt; 9000</span>
                    </Radio>
                    <br />

                </RadioGroup>                 
            </div>

            <Divider />

            <div className={classes.FlightType}>
                <h2 className={classes.TypeHeader}>Flight Time</h2>

                {Object.keys(props.filterInfo.flightTime).map((time,index) => {
                    return (
                        <p key={index}>
                            <Checkbox 
                                checked={props.filterInfo.flightTime[time]}
                                onChange={() => props.flightTimeType(time)}
                            />
                            <span>{time}</span>
                        </p>
                    )
                })}

            </div>
        </div>
    );
}
 
export default flightFilter;