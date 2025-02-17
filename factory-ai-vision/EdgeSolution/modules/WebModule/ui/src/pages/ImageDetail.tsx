import React, { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';

import { getImages } from '../store/imageSlice';
import { getParts } from '../store/partSlice';
import { getCameras } from '../store/cameraSlice';

import ImageDetailComponent from '../components/ImageDetail/ImageDetail';

const ImagesDetail = () => {
  const { id: projectId } = useParams<{ id: string }>();

  const [loading, setLoading] = useState(true);

  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await Promise.all([
        dispatch(getImages({ freezeRelabelImgs: true, selectedProject: parseInt(projectId, 10) })),
        // We need part info for image list items
        dispatch(getParts()),
        dispatch(getCameras(false)),
      ]);
      setLoading(false);
    })();
  }, [dispatch, projectId]);

  if (loading) return <h1>Loading...</h1>;

  return <ImageDetailComponent />;
};

export default ImagesDetail;
