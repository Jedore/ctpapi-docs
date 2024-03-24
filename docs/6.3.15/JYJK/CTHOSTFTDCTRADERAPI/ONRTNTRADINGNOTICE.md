<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="d456f2ce-0118-45c7-aa6b-c86569c65877"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="740efd44-39fa-4bcd-842b-b6c9643e69ae"></span>
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
<span class="anchor" id="b0814bba-aea5-45e9-a62c-c3f827fb9739"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2e52d535-387f-490d-9369-93ec627072e0"></span>
## 4.FAQ
<p>无</p>
