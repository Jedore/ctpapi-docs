<p>询价通知，此接口暂时不用，目前使用的是行情的<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>。</p>
<span class="anchor" id="ac2afa57-e369-4c0c-8c5a-2e1af41ea375"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="ba3f738b-d12e-459d-b24c-398ca2376c26"></span>
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
<span class="anchor" id="41ea6b6f-3d75-44b3-928a-6f21617ee3b4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="eff0e4bd-bab6-479a-ac0c-cc0d19b810ee"></span>
## 4.FAQ
<p>无</p>
