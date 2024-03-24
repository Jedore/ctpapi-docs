<p>请求删除预埋撤单，对应响应OnRspRemoveParkedOrderAction。该函数用于删除已经报入但未触发的某笔预埋撤单，注意是预埋撤单，而不是预埋报单。删除预埋报单使用ReqRemoveParkedOrder。</p>
<span class="anchor" id="d7333560-0be1-4685-96f1-d2c5b7efb80d"></span>
## 1.函数原型
<p>virtual int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="b5c3a0f9-b90f-45c7-9ec3-9f4fa319d707"></span>
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
<p>ParkedOrderActionID：对应的要删除的预埋撤单编号</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ab0831f9-b6e3-4cf4-89fd-7741981a1dcd"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6bc106b5-b7e6-4b66-ad8e-c41bd84eee04"></span>
## 4.调用示例
<pre><code>CThostFtdcRemoveParkedOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ParkedOrderActionID, "1");  
m_pUserApi-&gt;ReqRemoveParkedOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c0583bd7-0053-4555-a5bf-ab9b74a47858"></span>
## 5.FAQ
<p>无</p>
