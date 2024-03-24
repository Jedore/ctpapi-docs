<p>请求删除预埋单，对应响应OnRspRemoveParkedOrder。该函数用于删除已经报入但未触发的某笔预埋报单，注意跟ReqRemoveParkedOrderAction的区别。</p>
<span class="anchor" id="8bc74a18-64e3-499d-a795-142a787348e9"></span>
## 1.函数原型
<p>virtual int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) = 0;</p>
<span class="anchor" id="726fd793-724f-4034-a7c0-afcc3048aeeb"></span>
## 2.参数
<p>pRemoveParkedOrder：删除预埋单</p>
<pre><code>struct CThostFtdcRemoveParkedOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///预埋报单编号
    TThostFtdcParkedOrderIDType ParkedOrderID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>ParkedOrderID：对应的预埋报单编号，指定要删除的预埋报单。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4b38f2e4-f420-4e7b-ada7-fd3dee0c1bdd"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="bba4103c-ecda-445f-b803-0a0aa111d759"></span>
## 4.示例调用
<pre><code>CThostFtdcRemoveParkedOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ParkedOrderID, "           5");
m_pUserApi-&gt;ReqRemoveParkedOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="e5da0eaf-3d7b-45bc-9bab-11871a341c6e"></span>
## 5.FAQ
<p>无</p>
