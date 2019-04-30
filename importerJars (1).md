
# HBase Importer

## Targets
* [Configuration Design](#config_design)
* [Parsing Config](#parsing)
* [Importer Reuse (Modify the previous importers)](#importer)


<h2 id="config_design">Configuration Design</h2>

> **5 sections in config.json**
>> * **input**: *required*
>> * **rowkey**: *optional*
>> * **cf**: *optional*
>> * **parse**: *optional*
>> * **delimiter**: *optional*
>
> "**$**" means dynamic variables
>
> **input**
>> * describe the headers of input csv
>> * type String[]
>> * e.g. 

```json
{
  "input": [
    "$SN",
    "$TIME",
    "$LINE",
    "$STATIONID",
    "$RESULT",
    "$OP",
    "$MO",
    "$GRP"
  ]
}
```

> **rowkey**
>> * rowkey settings
>> * type String[]
>> * default: 1<sup>st</sup> input
>> * e.g. 

```json
{
  "rowkey": [
    "timestamp",
    "$SN"
  ]
}
```

> **cf**
>> * column family settings
>> * type ArrayList<HashMap<String, Object>>
>> * default: "R" for cf, "ALL" for qualifier, join all column field in a row as value.
>> * e.g. 

```json
{
  "cf": [
    {
      "name": "P",
      "qualifier": {
        "TIME": ["$TIME"],
        "LINE": ["$LINE"],
        "STATIONID": ["$STATIONID"],
        "RESULT": ["$RESULT"],
        "OP": ["$OP"],
        "MO": ["$MO"],
        "GRP": ["$GRP"],
        "VAL": ["$VAL"]
      }
    }
  ]
}
```

> **parse**
>> * column family settings
>> * type HashMap<String, Object>
>> * default: new HashMap<String, Object>()
>> * e.g. 

```json
{
  "parse": {
    "KPBC": [
      {
        "predicate": "BC",
        "slice_sets": [
          {
            "input_column": "$KPSN",
            "output_column": "$VAL",
            "slice_list": [[0, 5], [6, 8]]
          }
        ]
      },
      {"predicate":...}
}
```

> **delimiter**
>> * delimiter settings
>> * type HashMap<String, String>
>> * default: "_" for rowkey, "," for value, ";" for parsed
>> * e.g. 

```json
{
  "delimiter": {
    "rowkey": "_",
    "value": ",",
    "parsed": ";"
  }
}
```

<h2 id="parsing">Parsing Config</h2>

<table>
  <tr>
    <td>Methods</td>
    <td>Description</td>
    <td>Tests</td>
  </tr>
  <tr>
    <td>void loadConfig(String src)</td>
    <td>read config.json</td>
    <td>
      <ul>
        <li>&#9745; config object not null</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>void parseInput(String key_input)</td>
    <td>get input config section or raise error if input section not found.</td>
    <td>
      <ul>
        <li>&#9745; get config</li>
        <li>&#9745; raise error</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>void parseRowkey(String key_rowkey)</td>
    <td>get rowkey config section or set default rowkey</td>
    <td>
      <ul>
        <li>&#9745; get config</li>
        <li>&#9745; default</li>
    </td>
  </tr><tr>
    <td>void parseColumnFamily(String key_cf)</td>
    <td>get cf config section or set default cf</td>
    <td>
      <ul>
        <li>&#9745; get config</li>
        <li>&#9745; default</li>
    </td>
  </tr>
  <tr>
    <td>void parseParse(String key_parse)</td>
    <td>get parse config section or set default parse</td>
    <td>
      <ul>
        <li>&#9745; get config</li>
        <li>&#9745; default</li>
    </td>
  </tr>
  <tr>
    <td>void parseDelimiter (String key_delimiter)</td>
    <td>get delimiter config section or set default delimiter</td>
    <td>
      <ul>
        <li>&#9745; get config</li>
        <li>&#9745; default</li>
    </td>
  </tr>
  <tr>
    <td>void parseConfig(String key)</td>
    <td>switch paramter to call the other parseMethod()</td>
    <td>
      <ul>
        <li>&#9745; callable</li>
        <li>&#9744; default</li>
    </td>
  </tr>
  <tr>
    <td>overloading constructor</td>
    <td>extend arguments to set hbase api</td>
    <td>
      <ul>
        <li>&#9745; DEBUG</li>
        <li>&#9745; Each_File_Delay</li>
        <li>&#9745; Flush_Line_Limit</li>
        <li>&#9745; WriteBufferSize</li>
    </td>
  </tr>
  <tr>
    <td>JSONObjectToHashMap</td>
    <td>recursive method, for parsing multiple class of config section</td>
    <td>
      <ul>
        <li>&#9744; ToHashMap</li>
        <li>&#9744; ToArrayList</li>
    </td>
  </tr>
</table>

<h2 id="importer">Importer Reuse (Modify the previous importers)</h2>
*pending . . .*