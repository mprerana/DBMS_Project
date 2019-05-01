import React from 'react';
import { Skeleton } from 'antd';

import classes from './Skeleton.module.css';

const skeleton = (props) => {
    return (  
        <div className={classes.AdjustSkeleton}>
            <Skeleton active/>
        </div>
    );
}
 
export default skeleton;