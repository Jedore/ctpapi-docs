<p>询价通知，此接口暂时不用，目前使用的是行情的<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<span class="anchor" id="c39e31d2-35ca-4bd6-97e6-ac9c3e5944c9"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="1f81e5a3-6f4f-4d2a-b8fe-ed9ed49deed5"></span>
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
<span class="anchor" id="dcc4c5b0-54bc-4909-9dc0-a5cbe688da52"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="133ac9d4-43a0-4018-bfaa-1472becc3133"></span>
## 4.FAQ
<p>无</p>
