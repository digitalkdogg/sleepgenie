import React from "react"

import styles from './TopBar.module.css';

const TopBar = () => {
  return (
    <div id = "header" className =  {styles.header + " flex justify-content-center"}>
    Top bar
    </div>
  )
};

export default TopBar;