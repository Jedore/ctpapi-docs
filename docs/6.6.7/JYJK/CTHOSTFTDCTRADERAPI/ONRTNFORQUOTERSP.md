<p>询价通知，此接口暂时不用，目前使用的是行情的<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<span class="anchor" id="afc83d39-100a-4725-abe0-2913c4e360c4"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="34b2b23f-75a7-4dab-b1c0-78d002f667ed"></span>
## 2.参数
<p>pForQuoteRsp：发给做市商的询价请求</p>
<pre><code>struct CThostFtdcForQuoteRspField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///询价编号
    TThostFtdcOrderSysIDType    ForQuoteSysID;
    ///询价时间
    TThostFtdcTimeType  ForQuoteTime;
    ///业务日期
    TThostFtdcDateType  ActionDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>ForQuoteSysID：交易所给的一个询价编号，以此定位一笔询价。</p>
<span class="anchor" id="06cd36ab-a502-48a6-9915-2fbce9fd4e46"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ef88d9a1-633b-4cad-8ac7-2a780b592ce9"></span>
## 4.FAQ
<p>无</p>
