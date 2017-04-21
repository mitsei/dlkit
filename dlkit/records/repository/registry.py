from ..osid import registry as osid_registry

ASSET_GENUS_TYPES = {
    'manipulateable-asset-type': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.Asset',
        'identifier': 'manipulateable-asset-type',
        'display_name': 'Manipulatable Asset Type',
        'display_label': 'Manip Asset Type',
        'description': 'Asset type for a 3D manipulatable object',
        'domain': 'repository.Asset'},
    'ortho3d-asset-type': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.Asset',
        'identifier': 'ortho3d-asset-type',
        'display_name': 'Manipulatable Asset Type',
        'display_label': 'Manip Asset Type',
        'description': 'Asset type for a 3D manipulatable object',
        'domain': 'repository.Asset'},
    'ortho-view-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.Asset',
        'identifier': 'ortho-view-asset',
        'display_name': 'Orthographic View Asset Type',
        'display_label': 'OV Asset Type',
        'description': 'Asset type for an orthographic view image',
        'domain': 'repository.Asset'},
    'ortho-view-set-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.Asset',
        'identifier': 'ortho-view-set-asset',
        'display_name': 'Orthographic View Asset Type',
        'display_label': 'OV Asset Type',
        'description': 'Asset type for an orthographic view image',
        'domain': 'repository.Asset'},
    'edx-image-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-genus-type',
        'identifier': 'edx-img',
        'display_name': 'edX Image',
        'display_label': 'edX Image',
        'description': 'An image found in an edx course',
        'domain': 'repository.Asset'
    },
    'edx-file-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-genus-type',
        'identifier': 'edx-file',
        'display_name': 'edX File',
        'display_label': 'edX File',
        'description': 'A file found in an edx course',
        'domain': 'repository.Asset'
    },
    'fbw-image-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-genus-type',
        'identifier': 'fbw-image-asset',
        'display_name': 'FbW Image',
        'display_label': 'FbW Image',
        'description': 'An image for a Fly-by-Wire problem',
        'domain': 'repository.Asset'
    },
    'image': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-genus-type',
        'identifier': 'image',
        'display_name': 'Image',
        'display_label': 'Image',
        'description': 'An image',
        'domain': 'repository.Asset'
    },
    'audio': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-genus-type',
        'identifier': 'audio',
        'display_name': 'Audio',
        'display_label': 'Audio',
        'description': 'An audio',
        'domain': 'repository.Asset'
    }
}

ASSET_RECORD_TYPES = {
    'edx-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-record-type',
        'identifier': 'edx-asset',
        'display_name': 'edX Asset',
        'display_label': 'edX Asset',
        'description': 'Repository Asset record extension for edX content',
        'domain': 'repository.Asset',
        'module_path': 'dlkit.records.repository.edx.edx_assets',
        'object_record_class_name': 'edXAssetRecord',
        'form_record_class_name': 'edXAssetFormRecord',
        'query_record_class_name': 'edXAssetQueryRecord'
    },
}

ASSET_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

ASSET_CONTENT_GENUS_TYPES = {
    'edx-text-asset': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-type',
        'identifier': 'edx-text-asset-content',
        'display_name': 'edX Text Asset Content',
        'display_label': 'edX Text Asset Content',
        'description': 'An Asset Content that include text for edX',
        'domain': 'repository.AssetContent'},
    'manipulateable-asset-content': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.AssetContent',
        'identifier': 'manipulateable-asset-content',
        'display_name': 'Manipulatable Asset Content Type',
        'display_label': 'Manip Asset Content Type',
        'description': 'Asset Content type for a 3D manipulatable object',
        'domain': 'repository.AssetContent'},
    'ortho-view-asset-content': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.AssetContent',
        'identifier': 'ortho-view-asset-content',
        'display_name': 'Orthographic View Asset Content Type',
        'display_label': 'OV Asset Type',
        'description': 'AssetContent type for an orthographic view image',
        'domain': 'repository.AssetContent'},
    'ortho-view-set-small': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.AssetContent',
        'identifier': 'ortho-view-set-small',
        'display_name': 'Orthographic View Set Small Asset Type',
        'display_label': 'OV Set Small Asset Type',
        'description': 'AssetContent type for a small orthographic view set image',
        'domain': 'repository.AssetContent'},
    'ortho-view-set-large': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository.AssetContent',
        'identifier': 'ortho-view-set-large',
        'display_name': 'Orthographic View Set Large Asset Type',
        'display_label': 'OV Set Small Asset Type',
        'description': 'AssetContent type for a small orthographic view set image',
        'domain': 'repository.AssetContent'},
    'video': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-asset-content',
        'identifier': 'video',
        'display_name': 'edX video asset',
        'display_label': 'edX video asset',
        'description': 'An edX video',
        'domain': 'repository.AssetContent'
    },
    'discussion': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-asset-content',
        'identifier': 'discussion',
        'display_name': 'edX discussion',
        'display_label': 'edX discussion',
        'description': 'A discussion type asset',
        'domain': 'repository.AssetContent'
    },
    'wiki': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-asset-content',
        'identifier': 'wiki',
        'display_name': 'edX course wiki',
        'display_label': 'edX course wiki',
        'description': 'edX wiki asset',
        'domain': 'repository.AssetContent'
    },
    'html': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-asset-content',
        'identifier': 'html',
        'display_name': 'edX HTML content',
        'display_label': 'edX HTML content',
        'description': 'HTML content',
        'domain': 'repository.AssetContent'
    },
    'videoalpha': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-asset-content',
        'identifier': 'videoalpha',
        'display_name': 'edX video',
        'display_label': 'edX video',
        'description': 'Deprecated video content (use video tag)',
        'domain': 'repository.AssetContent'
    },
    'png': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'png',
        'display_name': 'Image/PNG',
        'display_label': 'Image/PNG',
        'description': 'A PNG image',
        'domain': 'repository.AssetContent'
    },
    'jpg': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'jpg',
        'display_name': 'Image/JPG',
        'display_label': 'Image/JPG',
        'description': 'A JPG image',
        'domain': 'repository.AssetContent'
    },
    'svg': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'svg',
        'display_name': 'Image/SVG',
        'display_label': 'Image/SVG',
        'description': 'An SVG image',
        'domain': 'repository.AssetContent'
    },
    'wav': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'wav',
        'display_name': 'Audio/WAV',
        'display_label': 'Audio/WAv',
        'description': 'An audio WAV file',
        'domain': 'repository.AssetContent'
    },
    'latex': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'latex',
        'display_name': 'application/x-tex',
        'display_label': 'application/x-tex',
        'description': 'LaTeX content',
        'domain': 'repository.AssetContent'
    },
    'json': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'json',
        'display_name': 'application/json',
        'display_label': 'application/json',
        'description': 'JSON content',
        'domain': 'repository.AssetContent'
    },
    'javascript': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'javascript',
        'display_name': 'application/javascript',
        'display_label': 'application/javascript',
        'description': 'JavaScript content',
        'domain': 'repository.AssetContent'
    },
    'generic': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'generic',
        'display_name': 'Content/Generic',
        'display_label': 'Content/Generic',
        'description': 'Generic content',
        'domain': 'repository.AssetContent'
    },
    'mp3': {
        'authority': 'iana.org',
        'namespace': 'asset-content-genus-type',
        'identifier': 'mp3',
        'display_name': 'audio/mpeg',
        'display_label': 'audio/mpeg',
        'description': 'MP3 content',
        'domain': 'repository.AssetContent'
    },
    'alt-text': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-genus-type',
        'identifier': 'alt-text',
        'display_name': 'Alt text',
        'display_label': 'Alt text',
        'description': 'Alt text for image tags',
        'domain': 'repository.AssetContent'
    },
    'media-description': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-genus-type',
        'identifier': 'media-description',
        'display_name': 'Description',
        'display_label': 'Description',
        'description': 'Description for media tags',
        'domain': 'repository.AssetContent'
    },
    'vtt': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-genus-type',
        'identifier': 'vtt',
        'display_name': 'Video caption file',
        'display_label': 'Video caption file',
        'description': 'Video caption file',
        'domain': 'repository.AssetContent'
    },
    'transcript': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-genus-type',
        'identifier': 'transcript',
        'display_name': 'Video / Audio Transcript file',
        'display_label': 'Video / Audio Transcript file',
        'description': 'Video / Audio Transcript file',
        'domain': 'repository.AssetContent'
    }
}

ASSET_CONTENT_RECORD_TYPES = {
    'asset-content-text': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'asset-content-text',
        'display_name': 'Asset Content Text',
        'display_label': 'Asset Content Text',
        'description': 'Repository Asset Content record extension for Asset Contents ' +
                       'with text',
        'domain': 'assessment.AssetContent',
        'module_path': 'dlkit.records.repository.basic.simple_records',
        'object_record_class_name': 'AssetContentTextRecord',
        'form_record_class_name': 'AssetContentTextFormRecord'},

    'edx-asset-content-text-files': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'edx-asset-content-text-files',
        'display_name': 'edX Asset Content Text with Files',
        'display_label': 'edX Asset Content Text with Files',
        'description': 'Repository Asset Content record extension for Asset Contents with ' +
                       'text and files',
        'domain': 'assessment.AssetContent',
        'module_path': 'dlkit.records.repository.edx.edx_assets',
        'object_record_class_name': 'edXAssetContentRecord',
        'form_record_class_name': 'edXAssetContentFormRecord'},

    'vcb-video-timestamp': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'vcb-video-timestamp',
        'display_name': 'VCB video timestamps',
        'display_label': 'VCB video timestamps',
        'description': 'AssetContent record extension for storing start and end timestamps ' +
                       'for video',
        'domain': 'repository.AssetContent',
        'module_path': 'dlkit.records.repository.vcb.vcb_records',
        'object_record_class_name': 'TimeStampRecord',
        'form_record_class_name': 'TimeStampFormRecord'},

    'multi-language-alt-texts': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'multi-language-alt-texts',
        'display_name': 'Alt text',
        'display_label': 'Alt text',
        'description': 'AssetContent record extension for storing alt text',
        'domain': 'repository.AssetContent',
        'module_path': 'dlkit.records.repository.basic.media_accessibility',
        'object_record_class_name': 'AssetContentMultiLanguageAltTextRecord',
        'form_record_class_name': 'AssetContentMultiLanguageAltTextFormRecord'},

    'multi-language-media-descriptions': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'multi-language-media-descriptions',
        'display_name': 'Media Description',
        'display_label': 'Media Description',
        'description': 'AssetContent record extension for storing Media Descriptions',
        'domain': 'repository.AssetContent',
        'module_path': 'dlkit.records.repository.basic.media_accessibility',
        'object_record_class_name': 'AssetContentMultiLanguageMediaDescriptionRecord',
        'form_record_class_name': 'AssetContentMultiLanguageMediaDescriptionFormRecord'},

    'multi-language-vtt-files': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'multi-language-vtt-files',
        'display_name': 'VTT Caption Files',
        'display_label': 'VTT Caption Files',
        'description': 'AssetContent record extension for storing multi-language caption files',
        'domain': 'repository.AssetContent',
        'module_path': 'dlkit.records.repository.basic.media_accessibility',
        'object_record_class_name': 'AssetContentMultiLanguageVTTRecord',
        'form_record_class_name': 'AssetContentMultiLanguageVTTFormRecord'},

    'multi-language-transcript-files': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'asset-content-record-type',
        'identifier': 'multi-language-transcript-files',
        'display_name': 'Transcript Files',
        'display_label': 'Transcript Files',
        'description': 'AssetContent record extension for storing multi-language transcript files',
        'domain': 'repository.AssetContent',
        'module_path': 'dlkit.records.repository.basic.media_accessibility',
        'object_record_class_name': 'AssetContentMultiLanguageTranscriptRecord',
        'form_record_class_name': 'AssetContentMultiLanguageTranscriptFormRecord'},
}

ASSET_CONTENT_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

COMPOSITION_GENUS_TYPES = {
    'course': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'course',
        'display_name': 'edX Composition Course',
        'display_label': 'edX Composition Course',
        'description': 'Wrapper for an edX course',
        'domain': 'repository.Composition'
    },
    'offering': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'offering',
        'display_name': 'edX Composition Course Offering',
        'display_label': 'edX Composition Course Offering',
        'description': 'Wrapper for an edX course offering',
        'domain': 'repository.Composition'
    },
    'chapter': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'chapter',
        'display_name': 'edX Composition Chapter',
        'display_label': 'edX Composition Chapter',
        'description': 'Wrapper for an edX chapter',
        'domain': 'repository.Composition'
    },
    'sequential': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'sequential',
        'display_name': 'edX Composition Sequential',
        'display_label': 'edX Composition Sequential',
        'description': 'Wrapper for an edX sequential',
        'domain': 'repository.Composition'
    },
    'split_test': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'split_test',
        'display_name': 'edX Composition Split Test',
        'display_label': 'edX Composition Split Test',
        'description': 'Wrapper for an edX split_test',
        'domain': 'repository.Composition'
    },
    'vertical': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'vertical',
        'display_name': 'edX Composition Vertical',
        'display_label': 'edX Composition Vertical',
        'description': 'Wrapper for an edX vertical',
        'domain': 'repository.Composition'
    },
    'resource-node': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'resource-node',
        'display_name': 'edX Composition Resource Node',
        'display_label': 'edX Composition  Resource Node',
        'description': 'Sequestered wrapper for an edX resource node / asset',
        'domain': 'repository.Composition'
    },
    'error-deleted': {
        'authority': 'EDX.ORG',
        'namespace': 'edx-composition',
        'identifier': 'error-deleted',
        'display_name': 'edX Composition Was Deleted',
        'display_label': 'edX Composition Was Deleted',
        'description': 'Sequestered wrapper for an edX composition that was deleted',
        'domain': 'repository.Composition'
    },
}

COMPOSITION_RECORD_TYPES = {
    'edx-composition': {
        'authority': 'EDX.ORG',
        'namespace': 'repository-composition',
        'identifier': 'edx-composition',
        'display_name': 'edX Composition',
        'display_label': 'edX Composition',
        'description': 'Wrapper for things like chapter / vertical / split_test',
        'domain': 'repository.Composition',
        'module_path': 'dlkit.records.repository.edx.compositions',
        'object_record_class_name': 'EdXCompositionRecord',
        'form_record_class_name': 'EdXCompositionFormRecord',
        'query_record_class_name': 'EdXCompositionQueryRecord'
    },
    'edx-course-run': {
        'authority': 'EDX.ORG',
        'namespace': 'repository-composition',
        'identifier': 'edx-course-run',
        'display_name': 'edX Course Run Composition',
        'display_label': 'edX Course Run Composition',
        'description': 'Wrapper for a specific course run',
        'domain': 'repository.Composition',
        'module_path': 'dlkit.records.repository.edx.compositions',
        'object_record_class_name': 'EdXCourseRunCompositionRecord',
        'form_record_class_name': 'EdXCourseRunCompositionFormRecord'
    }
}

COMPOSITION_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

REPOSITORY_GENUS_TYPES = {
    'courses-root-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'courses-root-repo',
        'display_name': 'LORE Courses Root Repository',
        'display_label': 'LORE Courses Root Repository',
        'description': 'Repository that acts as parent of all LORE course repositories',
        'domain': 'repository.Repository'},
    'users-root-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'users-root-repo',
        'display_name': 'LORE Users Root Repository',
        'display_label': 'LORE Users Root Repository',
        'description': 'Repository that acts as parent of all LORE user repositories',
        'domain': 'repository.Repository'},
    'domain-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'domain-repo',
        'display_name': 'LORE Domain of Knowledge Repository',
        'display_label': 'LORE Domain of Knowledge Repository',
        'description': 'Repository that contains courses within a domain of knowledge',
        'domain': 'repository.Repository'},
    'course-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'course-repo',
        'display_name': 'LORE Course Repository',
        'display_label': 'LORE Course Repository',
        'description': 'Repository for a single course',
        'domain': 'repository.Repository'},
    'course-run-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'course-run-repo',
        'display_name': 'LORE Course Run Repository',
        'display_label': 'LORE Course Run Repository',
        'description': 'Repository for a run of a single course',
        'domain': 'repository.Repository'},
    'user-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-genus-type',
        'identifier': 'user-repo',
        'display_name': 'LORE User Personal Repository',
        'display_label': 'LORE User Personal Repository',
        'description': 'Repository for a user, they control AuthZ to this',
        'domain': 'repository.Repository'},
}

REPOSITORY_RECORD_TYPES = {
    'lore-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-record-type',
        'identifier': 'lore-repo',
        'display_name': 'LORE Repository',
        'display_label': 'LORE Repository',
        'description': 'Repository that matches LORE\'s expected attributes',
        'domain': 'repository.Repository',
        'module_path': 'dlkit.records.repository.lore.repository_extensions',
        'object_record_class_name': 'LoreRepositoryRecord',
        'form_record_class_name': 'LoreRepositoryFormRecord'},
    'course-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-record-type',
        'identifier': 'course-repo',
        'display_name': 'LORE Course Repository',
        'display_label': 'LORE Course Repository',
        'description': 'Repository for a single course',
        'domain': 'repository.Repository',
        'module_path': 'dlkit.records.repository.lore.repository_extensions',
        'object_record_class_name': 'LoreCourseRepositoryRecord',
        'form_record_class_name': 'LoreCourseRepositoryFormRecord'},
    'run-repo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'repository-record-type',
        'identifier': 'run-repo',
        'display_name': 'LORE Run Repository',
        'display_label': 'LORE Run Repository',
        'description': 'Repository for a single course run',
        'domain': 'repository.Repository',
        'module_path': 'dlkit.records.repository.lore.repository_extensions',
        'object_record_class_name': 'LoreCourseRunRepositoryRecord',
        'form_record_class_name': 'LoreCourseRunRepositoryFormRecord'},
}
