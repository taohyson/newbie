VACUUM;
VACUUM COMPANY;

PRAGMA auto_vacuum = NONE;  -- 0 means disable auto vacuum
PRAGMA auto_vacuum = INCREMENTAL;  -- 1 means enable incremental vacuum
PRAGMA auto_vacuum = FULL;  -- 2 means enable full auto vacuum