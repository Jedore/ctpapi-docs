<p>请求查询签约银行</p>
<p>响应: OnRspQryContractBank</p>
<span class="anchor" id="50e71573-6343-4cc8-89f4-7fcaf99bc53d"></span>
## 1.函数原型
<p>virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;</p>
<span class="anchor" id="044f0268-8ee0-4d2d-a9ab-eb1eac4ea06a"></span>
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
<span class="anchor" id="f3a08cb9-69ed-4087-90d9-24ae636d17bc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2250d147-9ad2-4916-b092-76173a59f821"></span>
## 4.调用示例
<pre><code>CThostFtdcQryContractBankField a = { 0 };
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQryContractBank(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="030315b2-0ac8-4fe4-b6a8-940b55fb062f"></span>
## 5.FAQ
<p>无</p>
