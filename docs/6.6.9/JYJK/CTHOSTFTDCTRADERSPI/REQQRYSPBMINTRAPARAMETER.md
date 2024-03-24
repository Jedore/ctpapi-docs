<p>请求SPBM品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a></p>
<span class="anchor" id="38886918-f2aa-46f4-92f3-ca8787b7ede5"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMIntraParameter(CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="ff35bbe9-b157-4014-8b03-0d2a8d7ad3b6"></span>
## 2.参数
<p>pQrySPBMIntraParameter：SPBM品种内对锁仓折扣参数查询</p>
<pre><code>struct CThostFtdcQrySPBMIntraParameterField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="5ced14d6-0f49-4d73-a110-e1ee1a5cecb4"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="70b58b24-0184-4382-9304-cc02ece3b685"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="91e7e859-d215-4eb8-aa5a-a3351ab5dc17"></span>
## 5.FAQ
<p>无</p>
