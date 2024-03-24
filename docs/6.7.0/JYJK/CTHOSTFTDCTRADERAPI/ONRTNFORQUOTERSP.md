<p>询价通知，此接口暂时不用，目前使用的是行情的<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<span class="anchor" id="4ba88170-9df1-44ff-8ca0-53328e2cceeb"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="485ee00d-82f0-4fae-8a07-082ac48a5f16"></span>
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
<span class="anchor" id="c9d05bf8-30d6-438e-8f98-4bb0da942090"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="be9713a3-54a1-448f-a181-584fa8a8acc8"></span>
## 4.FAQ
<p>无</p>
