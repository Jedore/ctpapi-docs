<p>请求查询结算信息确认响应，当执行ReqQrySettlementInfoConfirm后，该方法被调用。</p>
<span class="anchor" id="13d7cba0-6710-4247-ae8a-2bd5bc97821a"></span>
## 1.函数原型
<p>virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3c3239ec-5828-46b4-80fb-c1ff2f5011d5"></span>
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
<span class="anchor" id="58696497-a32e-40d4-83c2-605a900f5ca7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b682ec22-937b-47a7-90a2-4693c2d05c61"></span>
## 4.FAQ
<p>无</p>
