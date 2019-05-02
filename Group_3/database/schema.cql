CREATE KEYSPACE dairy_management WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': '2', 'datacenter2': '1'}  AND durable_writes = true;

CREATE TABLE dairy_management.purchase (
    uid bigint,
    billno bigint,
    accountno bigint,
    amount double,
    icode list<bigint>,
    mode text,
    qty list<double>,
    rate list<double>,
    time timestamp,
    PRIMARY KEY ((uid, billno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX purchase_time_idx ON dairy_management.purchase (time);
CREATE INDEX purchase_amount_idx ON dairy_management.purchase (amount);
CREATE INDEX purchase_mode_idx ON dairy_management.purchase (mode);
CREATE INDEX purchase_accountno_idx ON dairy_management.purchase (accountno);
CREATE INDEX purchase_billno_idx ON dairy_management.purchase (billno);
CREATE INDEX purchase_uid_idx ON dairy_management.purchase (uid);
CREATE INDEX purchase_icode_idx ON dairy_management.purchase (values(icode));

CREATE TABLE dairy_management.account (
    uid bigint,
    accountno bigint,
    aadharno text,
    address text,
    email text,
    name text,
    phone text,
    type text,
    PRIMARY KEY ((uid, accountno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX account_accountno_idx ON dairy_management.account (accountno);
CREATE INDEX account_uid_idx ON dairy_management.account (uid);
CREATE INDEX account_name_idx ON dairy_management.account (name);

CREATE TABLE dairy_management.users (
    uid bigint PRIMARY KEY,
    email text,
    phash text,
    salt text,
    uname text
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX users_email_idx ON dairy_management.users (email);
CREATE INDEX users_uname_idx ON dairy_management.users (uname);

CREATE TABLE dairy_management.msales (
    uid bigint,
    msno bigint,
    accountno bigint,
    amount double,
    clr int,
    date date,
    fat double,
    qty double,
    shift int,
    PRIMARY KEY ((uid, msno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX msales_accountno_idx ON dairy_management.msales (accountno);
CREATE INDEX msales_msno_idx ON dairy_management.msales (msno);
CREATE INDEX msales_qty_idx ON dairy_management.msales (qty);
CREATE INDEX msales_uid_idx ON dairy_management.msales (uid);
CREATE INDEX msales_date_idx ON dairy_management.msales (date);
CREATE INDEX msales_amount_idx ON dairy_management.msales (amount);

CREATE TABLE dairy_management.receipt (
    uid bigint,
    rno bigint,
    accountno bigint,
    amount double,
    mode text,
    remarks text,
    time timestamp,
    PRIMARY KEY ((uid, rno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX receipt_accountno_idx ON dairy_management.receipt (accountno);
CREATE INDEX receipt_rno_idx ON dairy_management.receipt (rno);
CREATE INDEX receipt_uid_idx ON dairy_management.receipt (uid);
CREATE INDEX receipt_mode_idx ON dairy_management.receipt (mode);

CREATE TABLE dairy_management.sales (
    uid bigint,
    billno bigint,
    accountno bigint,
    amount double,
    icode list<bigint>,
    mode text,
    qty list<double>,
    rate list<double>,
    time timestamp,
    PRIMARY KEY ((uid, billno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX sales_icode_idx ON dairy_management.sales (values(icode));
CREATE INDEX sales_time_idx ON dairy_management.sales (time);
CREATE INDEX sales_accountno_idx ON dairy_management.sales (accountno);
CREATE INDEX sales_mode_idx ON dairy_management.sales (mode);
CREATE INDEX sales_uid_idx ON dairy_management.sales (uid);
CREATE INDEX sales_amount_idx ON dairy_management.sales (amount);
CREATE INDEX sales_billno_idx ON dairy_management.sales (billno);

CREATE TABLE dairy_management.auth (
    uid bigint,
    authtoken text,
    time timestamp,
    PRIMARY KEY (uid, authtoken)
) WITH CLUSTERING ORDER BY (authtoken ASC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 86400
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';

CREATE TABLE dairy_management.item (
    uid bigint,
    icode bigint,
    available double,
    name text,
    rate double,
    PRIMARY KEY (uid, icode)
) WITH CLUSTERING ORDER BY (icode ASC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX item_available_idx ON dairy_management.item (available);
CREATE INDEX item_name_idx ON dairy_management.item (name);

CREATE TABLE dairy_management.rates (
    uid bigint,
    fat double,
    clr int,
    rate double,
    PRIMARY KEY ((uid, fat), clr)
) WITH CLUSTERING ORDER BY (clr ASC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX rates_uid_idx ON dairy_management.rates (uid);
CREATE INDEX rates_fat_idx ON dairy_management.rates (fat);

CREATE TABLE dairy_management.mcollection (
    uid bigint,
    mcno bigint,
    accountno bigint,
    amount double,
    clr int,
    date date,
    fat double,
    qty double,
    shift int,
    PRIMARY KEY ((uid, mcno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX mcollection_qty_idx ON dairy_management.mcollection (qty);
CREATE INDEX mcollection_amount_idx ON dairy_management.mcollection (amount);
CREATE INDEX mcollection_date_idx ON dairy_management.mcollection (date);
CREATE INDEX mcollection_mcno_idx ON dairy_management.mcollection (mcno);
CREATE INDEX mcollection_uid_idx ON dairy_management.mcollection (uid);
CREATE INDEX mcollection_accountno_idx ON dairy_management.mcollection (accountno);

CREATE TABLE dairy_management.expense (
    uid bigint,
    entryno bigint,
    amount double,
    remarks text,
    time timestamp,
    PRIMARY KEY ((uid, entryno))
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
CREATE INDEX expense_time_idx ON dairy_management.expense (time);
CREATE INDEX expense_amount_idx ON dairy_management.expense (amount);
CREATE INDEX expense_uid_idx ON dairy_management.expense (uid);
CREATE INDEX expense_entryno_idx ON dairy_management.expense (entryno);


