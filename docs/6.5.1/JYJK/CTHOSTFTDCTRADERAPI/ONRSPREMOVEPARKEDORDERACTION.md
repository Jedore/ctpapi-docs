<p>删除预埋撤单响应，当执行ReqRemoveParkedOrderAction后，该方法被调用。</p>
<span class="anchor" id="1d233ea7-9013-424a-b59e-507e6bcf2ba0"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a5826fd9-2183-4eda-8700-15a991366f45"></span>
## 2.参数
<p>pRemoveParkedOrderAction：删除预埋撤单</p>
<pre><code>struct CThostFtdcRemoveParkedOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///预埋撤单编号
    TThostFtdcParkedOrderActionIDType ParkedOrderActionID;
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
<span class="anchor" id="a6adf4ee-6c69-4bcd-bf83-1e7c518d9949"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1ef96ae0-9b81-4181-8f6b-a3b022c830af"></span>
## 4.FAQ
<p>无</p>
