<p>请求查询签约银行</p>
<p>响应: OnRspQryContractBank</p>
<span class="anchor" id="3bc86142-952e-4ae6-b3f9-a25e28ba7e84"></span>
## 1.函数原型
<p>virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;</p>
<span class="anchor" id="a10679a0-cba8-4f54-a2a2-0b0cce9d2916"></span>
## 2.参数
<p>pQryContractBank：查询签约银行请求</p>
<pre><code>struct CThostFtdcQryContractBankField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="5fd2dfa1-3499-4eca-b1f2-50358d5582b8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fa432937-b17f-4b9e-9f65-9494060cf6ac"></span>
## 4.调用示例
<pre><code>CThostFtdcQryContractBankField a = { 0 };
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQryContractBank(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="fdf64384-6db5-4a98-a3ba-96f5dda40a46"></span>
## 5.FAQ
<p>无</p>
