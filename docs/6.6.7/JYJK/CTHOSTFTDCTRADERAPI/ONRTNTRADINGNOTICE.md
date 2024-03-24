<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="0db1cd97-52b7-4918-b8fd-70fed49484fd"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="49409853-fb33-4009-afd4-881e995527b7"></span>
## 2.参数
<p>pTradingNoticeInfo：用户事件通知信息</p>
<pre><code>struct CThostFtdcTradingNoticeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息正文
    TThostFtdcContentType FieldContent;
    ///序列系列号
    TThostFtdcSequenceSeriesType SequenceSeries;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<span class="anchor" id="613d26e4-b333-4094-99c2-deaf3ea28bd3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0fe81ebf-7c60-4e2c-9b52-d47e4e36bf79"></span>
## 4.FAQ
<p>无</p>
