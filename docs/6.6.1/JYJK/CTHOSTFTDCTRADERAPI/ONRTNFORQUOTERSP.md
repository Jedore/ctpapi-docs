<p>询价通知，此接口暂时不用，目前使用的是行情的OnRtnForQuoteRsp。</p>
<span class="anchor" id="e5859114-496f-4c6f-8919-6d25e55562eb"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="2c668883-6ff7-41e2-840f-4e95e75b4bef"></span>
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
<span class="anchor" id="609555fa-4740-4d12-ad01-3ea3d0ae895c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ef2e75af-08e8-4c67-a3e5-1d023252c7c6"></span>
## 4.FAQ
<p>无</p>
