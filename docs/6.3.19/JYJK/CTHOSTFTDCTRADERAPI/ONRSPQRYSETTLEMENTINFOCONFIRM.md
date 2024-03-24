<p>请求查询结算信息确认响应，当执行ReqQrySettlementInfoConfirm后，该方法被调用。</p>
<span class="anchor" id="81d7df3c-94c9-4e5e-a6de-54c432efcdcc"></span>
## 1.函数原型
<p>virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="891e9c50-f64e-4b39-ad6c-001ede868344"></span>
## 2.参数
<p>pSettlementInfoConfirm：投资者结算结果确认信息</p>
<pre><code>struct CThostFtdcSettlementInfoConfirmField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///确认日期
    TThostFtdcDateType ConfirmDate;
    ///确认时间
    TThostFtdcTimeType ConfirmTime;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
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
<span class="anchor" id="04f7fce1-d1ee-4729-826e-05410297194f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="af393b52-8724-4bd6-be53-90bd82c15c3e"></span>
## 4.FAQ
<p>无</p>
