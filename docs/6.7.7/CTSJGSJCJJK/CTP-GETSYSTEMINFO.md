<p>获取AES加密和RSA加密的终端信息。该函数来自采集终端信息的动态链接库（安卓版的函数名和使用方法较windows和linux有所区别，请注意阅读API包相关说明文档）。</p>
<p>仅中继模式下的客户端需要调用此函数来采集信息。中继需要将客户端采集到的信息上报给CTP。</p>
<p>直连模式下，登录的时候自动采集并上报终端信息，所以无需调用。</p>
<blockquote>
<p>采集库在win、linux、android上不是线程安全的，不要并发调用，ios是线程安全的</p>
<p>采集库暂时不采集IPv6地址</p>
</blockquote>
<span class="anchor" id="be9e4b0b-b0e7-4d5d-88f7-d78ea3fdab10"></span>
## 1.函数原型
<p>int CTP_GetSystemInfo(char* pSystemInfo, int&amp; nLen);</p>
<span class="anchor" id="243b5642-8d2b-4762-8d41-6d52e8a9ac9c"></span>
## 2.参数
<p>pSystemInfo：空间需要调用者自己分配至少270个字节。</p>
<blockquote>
<p>要注意这并不是一个字符串，而是数组，因为多次加密后可能断串，<strong>使用memcpy拷贝值而不是strcpy</strong>。</p>
</blockquote>
<p>nLen：获取到的采集信息的长度。</p>
<span class="anchor" id="3b31faaf-2ad2-4223-8d11-b75a2f8db3db"></span>
## 3.返回
<p>0 为正确，非0为错误。</p>
<p>具体哪个采集项有问题需要做如下判断：</p>
<pre><code>windows返回值定义:
    从低位开始分别标示 终端信息 -&gt;系统盘分区信息
    返回值 &amp; （0x01 &lt;&lt; 0） 不为0 表示终端类型未采集到
    返回值 &amp; （0x01 &lt;&lt; 1） 不为0 表示 信息采集时间获取异常
    返回值 &amp; （0x01 &lt;&lt; 2） 不为0 表示ip 获取失败  （采集多个相同类型信息的场景有一个采集到 即表示采集成功）
    返回值 &amp; （0x01 &lt;&lt; 3） 不为0 表示mac 获取失败
    返回值 &amp; （0x01 &lt;&lt; 4） 不为0 表示 设备名 获取失败
    返回值 &amp; （0x01 &lt;&lt; 5） 不为0 表示 操作系统版本 获取失败
    返回值 &amp; （0x01 &lt;&lt; 6） 不为0 表示 硬盘序列号 获取失败
    返回值 &amp; （0x01 &lt;&lt; 7） 不为0 表示 CPU序列号 获取失败
    返回值 &amp; （0x01 &lt;&lt; 8） 不为0 表示 BIOS 获取失败
    返回值 &amp; （0x01 &lt;&lt; 9） 不为0 表示 系统盘分区信息 获取失败
Linux返回值定义：
    从低位开始分别标示 终端信息 -&gt; BIOS信息
    返回值 &amp; （0x01 &lt;&lt; 0） 不为0 表示终端类型未采集到
    返回值 &amp; （0x01 &lt;&lt; 1） 不为0 表示 信息采集时间获取异常
    返回值 &amp; （0x01 &lt;&lt; 2） 不为0 表示ip 获取失败  （采集多个相同类型信息的场景有一个采集到 即表示采集成功）
    返回值 &amp; （0x01 &lt;&lt; 3） 不为0 表示mac 获取失败
    返回值 &amp; （0x01 &lt;&lt; 4） 不为0 表示 设备名 获取失败
    返回值 &amp; （0x01 &lt;&lt; 5） 不为0 表示 操作系统版本 获取失败
    返回值 &amp; （0x01 &lt;&lt; 6） 不为0 表示 硬盘序列号 获取失败
    返回值 &amp; （0x01 &lt;&lt; 7） 不为0 表示 CPU序列号 获取失败
    返回值 &amp; （0x01 &lt;&lt; 8） 不为0 表示 BIOS 获取失败
</code></pre>
<span class="anchor" id="282db23b-a443-4f41-a3d6-a592e755371b"></span>
## 4.调用示例
<pre><code>char pSystemInfo[344];
int len;
CTP_GetSystemInfo(pSystemInfo, len);
</code></pre>
<span class="anchor" id="a168faa0-43e3-445c-9032-783f87997ae7"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">终端采集到的信息，保存到数据库里后显示为乱码，怎么办？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可以使用BASE64转码成可见字符后再存储。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在windows下调用该函数后，控制台窗口打印出一些日志，提示找不到wmic之类的信息，这个有关系吗？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>有关系，采集函数需要调用相关windows组件来采集设备信息，如果没有对应组件，则会采集不到相应信息，不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在linux下调用该函数后，控制台窗口会输出一些报错日志，提示没有权限之类的错误，这个有关系吗？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>有关系，采集函数需要调用linux命令来采集设备信息，如果没有对应权限，则会采集不到相应信息，不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
