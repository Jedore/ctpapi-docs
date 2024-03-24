<p>请求查询转帐银行</p>
<p>响应: OnRspQryTransferBank</p>
<span class="anchor" id="7f703e13-6c3f-490f-9752-0c18f0f31a91"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="7d754553-67fe-42ff-8704-6fbf768ab28b"></span>
## 2.参数
<p>pQryTransferBank：查询转帐银行</p>
<pre><code>struct CThostFtdcQryTransferBankField
{
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="74fce27e-0246-48bc-b8a5-9d295324a42c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ac7686d4-a5d4-44f6-920a-0db8393b0462"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5e89e620-b82c-470b-a562-4f8f271c835b"></span>
## 5.FAQ
<p>无</p>
