<p>请求查询交易通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADINGNOTICE/">ReqQryTradingNotice</a>后，该方法被调用。</p>
<span class="anchor" id="5d15865b-1bc8-4dc6-a236-5b3de9144269"></span>
## 1.函数原型
<p>virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8aa54fa6-e0ad-405d-aef4-16dae3c5cf15"></span>
## 2.参数
<p>pTradingNotice：用户事件通知</p>
<pre><code>struct CThostFtdcTradingNoticeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///序列系列号
    TThostFtdcSequenceSeriesType SequenceSeries;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///消息正文
    TThostFtdcContentType FieldContent;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="4de8387a-85e4-474f-bd3b-ab42c437fc70"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9a0ca304-29a9-4a0c-a544-f096fc91309a"></span>
## 4.FAQ
<p>无</p>
