import React from 'react';
import Image from 'next/image'

import styles from './CardWithBanner.module.scss'

import cn from 'classnames'

export const CardWithBanner = ({image, name, bio, links, phone, email}) => {
    console.log(image)
  return (
    <article className={styles.wrapper}>
        {/* <Image src={image} width={150} height={150} alt="Аватарка" className={styles.image} /> */}
        <img src={image} alt="Аватарка" className={styles.image} />
        <div className={styles.banner}></div>
        <h1 className={styles.name}>{name}</h1>
        {bio && <p className={styles.bio}>{bio}</p>}
        <div className={styles.links}>
            {Object.keys(links).map(link => <a className={cn(styles.link, link)} href={links[link]} key={link}></a>)}
        </div>
        <hr className={styles.line} />
        {phone && <a className={styles.phone}>{phone}</a>}
        {email && <a href={`mailto: ${email}`} className={styles.email}>{email}</a>}
    </article>
  );
};
