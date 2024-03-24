<p>请求查询转帐银行</p>
<p>响应: OnRspQryTransferBank</p>
<span class="anchor" id="27fddbe5-459d-4d0d-8ab2-969f758c812d"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="8fda8aee-504e-4566-a64d-f5b8dcad7793"></span>
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
<span class="anchor" id="6223e1c1-a08b-4260-b330-e3578d4e3d25"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fbc186e3-3aae-4ad2-a180-78f134e43656"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4e4d8de8-50d4-4cce-a59b-6d3371d4c30b"></span>
## 5.FAQ
<p>无</p>
